from  odoo import models ,fields ,api
from odoo.exceptions import UserError


class TodoTask(models.Model):
    _name = "todo.task"
    _description = "todo task"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    active = fields.Boolean(default=True)
    task_name = fields.Char('Name', required=True)
    description=fields.Char(tracking=1)
    deu_date=fields.Date(tracking=1)
    expected_ticket_date = fields.Date()
    is_late = fields.Boolean()
    status=fields.Selection([
        ('new','New') ,('in_process','In process') ,('completed','Completed') ,('close','Close')
    ])
    estimated_time=fields.Integer()
    line_ids=fields.One2many('task.line','todo_id')
    tasker_id =fields.Many2one('tasker' ,tracking=1)
    assign_to = fields.Char( related='tasker_id.tasker_name')
    assign_to_id=fields.Many2one('res.partner')
    sequence_number = fields.Char(string='Task Sequence', readonly=True, copy=False, default='New')

    @api.model
    def create(self, vals):
        if vals.get('sequence_number', 'New') == 'New':
            vals['sequence_number'] = self.env['ir.sequence'].next_by_code('todo.task.sequence') or 'New'
        return super(TodoTask, self).create(vals)

    def action_new(self):
        for rec in self :
            rec.status='new'

    def action_in_process(self):
        for rec in self :
            rec.status="in_process"

    def action_completed(self):
        for rec in self :
            rec.status="completed"

    def action_close(self):
        for rec in self:
            rec.status = "close"

    def check_ticket_late_date(self):
         todo_ids=self.search([])
         for rec in todo_ids :
             if  rec.expected_ticket_date  and rec.expected_ticket_date<rec.deu_date :
                   rec.is_late = True

    def write(self, vals):
        for task in self:
            if task.status in ('completed', 'close'):
                raise UserError("Cannot update a completed or closed task.")
        return super(TodoTask, self).write(vals)
@api.constrains('line_ids')
def _check_time_smaller_estimated_time(self):
    for rec in self :
        if rec.line_ids.time < rec.estimated_time :
            print("_check_time_smaller_estimated_time")


class TaskLine(models.Model):
     _name = 'task.line'
     name=fields.Char('user name')
     description = fields.Text('Description')
     time = fields.Integer('Time')
     total_time=fields.Integer(compute ='_compute_total_time')
     todo_id=fields.Many2one('todo.task')

     @api.depends( 'time')
     def _compute_total_time(self):
         # line_ids = self.search([])
         for rec in self :
             rec.total_time+=rec.time



