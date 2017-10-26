# -*- coding: utf-8 -*-

from psycopg2 import IntegrityError

from odoo.tests.common import TransactionCase

from faker import Faker

from odoo.tools import mute_logger

fake = Faker()


class TestInvoice(TransactionCase):
    at_install = False
    post_install = True

    def setUp(self):
        super(TestInvoice, self).setUp()

    def test_res_partner_alias_upper(self):
        # Use 'budget.enduser.division to test mixin as mixin are just abstract models and division inherits from it'
        # Expected output is upper and no spaces

        # generates s random name (eg. John Doe)
        alias = fake.name()

        division_id = self.env['budget.enduser.division'].create({
            'name': fake.name(),
            'alias': alias
        })

        self.assertEqual(division_id.alias, alias.upper().replace(" ", ""))

        alias = fake.name()
        # generates s random name (eg. John Doe)

        division_id.write({
            'alias': alias
        })

        self.assertEqual(division_id.alias, alias.upper().replace(" ", ""))

    def test_res_partner_unique_create(self):
        # generates s random name (eg. John Doe)
        alias = fake.name()

        self.env['budget.enduser.division'].create({
            'name': fake.name(),
            'alias': alias
        })

        with self.assertRaises(IntegrityError), mute_logger('odoo.sql_db'):
            self.env['budget.enduser.division'].create({
                'name': fake.name(),
                'alias': alias
            })

    def test_res_partner_unique_write(self):
        # generates s random name (eg. John Doe)
        alias = fake.name()

        division01_id = self.env['budget.enduser.division'].create({
            'name': fake.name(),
            'alias': alias
        })

        division02_id = self.env['budget.enduser.division'].create({
            'name': fake.name(),
            'alias': fake.name()
        })

        with self.assertRaises(IntegrityError), mute_logger('odoo.sql_db'):
            division02_id.write({
                'alias': alias
            })
