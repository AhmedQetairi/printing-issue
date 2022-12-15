import json
from odoo import http
from odoo.addons.web.controllers.main import ReportController


class PrtReportController(http.Controller):

    @http.route('/contactus', type='http', auth="public")
    def report_download(self, data, token, context=None):
        res = super(PrtReportController, self).report_download(data, token, context)
        if json.loads(data)[2] in ('open', 'print'):
            res.headers['Content-Disposition'] = res.headers['Content-Disposition'].replace('attachment', 'inline')
        return res
        # return "Hello World"
