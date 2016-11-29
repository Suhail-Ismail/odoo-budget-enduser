# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Region(models.Model):
    _name = 'budget.enduser.region'
    _rec_name = 'alias'
    _description = 'Region'

    # BASIC FIELDS
    # ----------------------------------------------------------
    name = fields.Char(string='Region Name')
    alias = fields.Char(string='Alias')
    note = fields.Text(string='Note')
