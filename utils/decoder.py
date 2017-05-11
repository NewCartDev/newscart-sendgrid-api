# -*- coding: utf-8 -*-
"""NewsCartSendgridAPI Decoder
    This module contains utility classes for NewsCartSendgridAPI
"""
from base64 import b64decode
from urllib import unquote
from utils.logger import LOGGER

class Decoder(object):
    """
        A class used to decode given EncodeURI+Base64 ecnoded html.
        For docs on the Javascript implementation of Base64 visit:
            https://developer.mozilla.org/en-US/docs/Web/API/WindowBase64/Base64_encoding_and_decoding
        For docs on Javascript implementation of EncodeURIComponent visit:
            https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent
    """
    def __init__(self):
        """
        It is possible that multiple and or duplicate requests could be made to this service,
        so this class will implement a rudimentary memoization functionality
            Note:
                This is experimental and subject to removal
        """
        self.memo = {}

    def base64_to_html(self, encoded_html):
        """
            Decodes given encoded html into String
            Args:
                encoded_html (str): Base64 + URI Encoded Html
            Example:
                Decoder.base64ToHtml("JTNDaDElM0VIZWxsbyUyMFdvcmxkJTNDL2gxJTNF")
                <h1>Hello World</h1>
        """
        try:
            LOGGER.info('Attempting to decode %s', encoded_html)
            if encoded_html in self.memo:
                return self.memo[encoded_html]
            else:
                decoded_html = unquote(b64decode(encoded_html).decode())
                self.memo[encoded_html] = decoded_html
        except:
            LOGGER.error('Failed to decode %s', encoded_html)
            raise Exception('Failure to decode %s', encoded_html)

        return decoded_html
