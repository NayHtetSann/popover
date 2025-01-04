from odoo import http
from odoo.http import request


class PopOverController(http.Controller):

    @http.route('/fetch/images', type='json', auth='public')
    def fetch_image(self):
        popup_ids = request.env['dynamic.popup'].sudo().search([('active', '=', True)], order='sequence desc')
        responses = [[popup.image_size, popup.image] for popup in popup_ids]
        return responses
