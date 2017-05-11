from app import APP

class TestSendgridAPI:

    def setup(self):
        APP.config['TESTING'] = True
        self.test_app = APP.test_client()

    def test_get_ping(self):
        result = self.test_app.get('/templates/ping')
        assert '200' in result.data

    def test_it_should_return_404_for_unknown_route(self):
        result = self.test_app.get('/templates/wow')
        assert '404' in result.data
