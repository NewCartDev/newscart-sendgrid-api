""" NewsCartSendgridAPI Template Router Blueprint
"""
import urllib2
from flask import Blueprint, jsonify, request, current_app
from sendgrid import SendGridAPIClient
from services.template_builder import TemplateBuilder

TEMPLATE = Blueprint('template', __name__)

@TEMPLATE.route('/ping', methods=['GET'])
def handle_ping():
    """
        Route to check if service is alive
        GET to /templates/ping
            {status: 200, message: 'pong'}
    """
    return jsonify(status=200,message='pong'), 200


@TEMPLATE.route('/send-template', methods=['POST'])
def handle_send_template():
    """
        Params:
            Request Body:
                JSON object containing config and content of mailer to send
            Example:
                 POST templates/send-template
                    {
                     "recipients": ["email@address.com","email@address.com"],
                     "from": "dude@manwow.com",
                     "subject": "Yoh bruh",
                     "content": "JTNDaDElM0VsJTIwbyUyMGwlM0MvaDElM0U="
                    }
    """
    if request.json is None:
        return jsonify(status=400, message=('Config for template is required')), 400
    template_config = request.json
    template_builder = TemplateBuilder(template_config)
    template_builder.build_template()
    mailer = template_builder.get_template()
    sg_api = SendGridAPIClient(apikey=current_app.config['SENDGRID_API_KEY'])
    try:
        response = sg_api.client.mail.send.post(request_body=mailer)
    except urllib2.HTTPError as response_error:
        jsonify(status=response.status_code, message=response_error.read)
    return jsonify(status=response.status_code, message="email sent")

@TEMPLATE.route('/', defaults={'path': ''})
@TEMPLATE.route('/<path:path>')
def catch_all(path):
    """
        Catch all for unexpected requests
    """
    return jsonify(status=404, message=('Path %s does not exist' % path)), 404
