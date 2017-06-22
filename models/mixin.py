from odoo import models, fields, api


class Enduser(models.AbstractModel):
    _name = 'budget.enduser.mixin'
    _description = 'End User Mixin'

    # BASIC FIELDS
    # ----------------------------------------------------------
    division_id = fields.Many2one('budget.enduser.division', string="Division")
    section_id = fields.Many2one('budget.enduser.section', string="Section")
    sub_section_id = fields.Many2one('budget.enduser.sub.section', string="Sub Section")

    # ONCHANGE FIELDS
    @api.onchange('section_id')
    def _onchange_section_id(self):
        self.division_id = self.section_id.division_id

    @api.onchange('sub_section_id')
    def _onchange_sub_section_id(self):
        self.section_id = self.sub_section_id.section_id

