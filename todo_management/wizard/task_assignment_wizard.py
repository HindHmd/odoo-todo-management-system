from odoo import models, fields

class TaskAssignmentWizard(models.TransientModel):
    _name = 'task.assignment.wizard'
    _description = 'Bulk Task Assignment Wizard'

    employee_id = fields.Many2one('res.partner', string='Employee', required=True)
    task_ids = fields.Many2many('todo.task', string='Tasks')

    def assign_tasks(self):
        self.task_ids.write({'assign_to_id': self.employee_id.id})
        return {'type': 'ir.actions.act_window_close'}