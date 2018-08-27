from datetime import datetime

#from lxml import etree
from pprint import pprint

from lxml import etree
from zeep import Plugin

import config


class FastemsHeadersPlugin(Plugin):
    def _envelope_tostring(self, e):
        print('egress envelope', etree.tostring(e, pretty_print=True).decode("utf-8"))

    def ingress(self, envelope, http_headers, operation):
        """Tap incoming response"""
        return envelope, http_headers

    def egress(self, envelope, http_headers, operation, binding_options):
        """Tap outgoing request"""
        ignore_at = datetime.now().strftime('%m-%d-%Y %H:%M:%S %p')

        fastems_headers = {
            'Accept': '*/*',
            # 'SOAPAction': operation.soapaction,
            'Referer': 'http://%s/MMS5/DataManager.xap?ignore=%s' % (config.FASTEMS_HOST, ignore_at),
            'Accept-Language': 'en-US',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; McAfee; InfoPath.2)',
            'Host': config.FASTEMS_HOST,
            'DNT': '1',
            'Connection': 'Keep-Alive',
            'Cache-Control': 'no-cache'
        }

        return envelope, {**http_headers, **fastems_headers}
