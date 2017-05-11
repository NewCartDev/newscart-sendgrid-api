# -*- coding: utf-8 -*-
"""NewsCartSendgridAPI SendgridService
This module contains helper classes and methods for
interacting with the Sendgrid API

Documentation can be found here:
    https://sendgrid.com/docs/Integrate/Code_Examples/v2_Mail/python.html

Code Samples found here:
    https://github.com/sendgrid/sendgrid-python/blob/master/examples/helpers/mail/mail_example.py
"""
from utils.decoder import Decoder
from sendgrid.helpers.mail import Mail, Personalization, Email, Content

DECODER = Decoder()

class TemplateBuilder(object):
    """
        Helper class to build Sendgrid compatible Mailer Template
    """
    def __init__(self, config):
        if config is None:
            raise ValueError('Missing config for SendgridService Constructor')
        self.template_config = config
        self.template = None

    def build_template(self):
        """
            Builds mailer template based on given config
        """
        # Initialize mail object
        self.template = Mail()

        # Set From and Subject Line
        self.template.from_email = Email(email='newscart@newscart.co', name='NewsCart')
        self.template.subject = self.template_config['subject']

        # Add mailer recipients
        personalization = Personalization()
        for recipient in self.template_config['recipients']:
            personalization.add_to(Email(recipient))
        self.template.add_personalization(personalization)

        # Decode given HTML content
        mailer_html = DECODER.base64_to_html(self.template_config['content'])
        self.template.add_content(Content("text/html", mailer_html))

        self.template.reply_to = Email(self.template_config['from'])

    def get_template(self):
        """
            Returns configured mailer template
        """
        return self.template.get()
