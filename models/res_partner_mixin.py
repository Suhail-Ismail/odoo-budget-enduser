# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ResPartnerMixin(models.AbstractModel):
    _name = 'budget.enduser.res.partner.mixin'
    _description = 'Budget Enduser Res Partner Mixin'
    _rec_name = 'name'
    _inherits = {'res.partner': 'partner_id'}

    # BASIC FIELDS
    # ----------------------------------------------------------
    active = fields.Boolean(default=True)

    alias = fields.Char(string="Alias")
    remark = fields.Text(string='Remarks')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    partner_id = fields.Many2one('res.partner', required=True, ondelete='restrict', auto_join=True,
                                 string='Related Partner', help='Partner-related data of the user')
    # ONCHANGE FIELDS
    # ----------------------------------------------------------

    # COMPUTE FIELDS
    # ----------------------------------------------------------

    # CONSTRAINS
    # ----------------------------------------------------------
    _sql_constraints = [
        ('uniq', 'UNIQUE (alias)', 'Alias must be Unique'),
    ]

    # ACTION BUTTONS
    # ----------------------------------------------------------

    # POLYMORPH FUNCTIONS
    # ----------------------------------------------------------
    @api.multi
    def write(self, vals):
        if vals.get('alias', False):
            vals['alias'] = vals.get('alias').upper().replace(" ", "")
        return super(ResPartnerMixin, self).write(vals)

    @api.model
    def create(self, vals):
        if vals.get('alias', False):
            vals['alias'] = vals.get('alias').upper().replace(" ", "")
        return super(ResPartnerMixin, self).create(vals)
