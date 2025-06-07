from  odoo import models ,fields


class Tasker(models.Model):
    _name = "tasker"
    _description = "todo tasker"

    tasker_name = fields.Char('Name', required=True)


