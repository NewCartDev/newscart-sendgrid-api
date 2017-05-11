from utils.decoder import Decoder
from nose.tools import assert_equals


DECODER = Decoder()


def test_it_decodes_encoded_string():
    assert_equals(DECODER.base64_to_html("JTNDaDElM0VIZWxsbyUyMFdvcmxkJTNDL2gxJTNF"), "<h1>Hello World</h1>")
