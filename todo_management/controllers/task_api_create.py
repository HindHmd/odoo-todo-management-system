from odoo import http
from odoo.http import request, Response
import json

class TodoTaskAPICreate(http.Controller):

    @http.route('/api/tasks', auth='user', type='json', methods=['POST'])
    def create_task(self, **kwargs):
        task_data = request.jsonrequest
        new_task = request.env['todo.task'].create({
            'task_name': task_data.get('name'),
            'description': task_data.get('description'),
            'assign_to_id': task_data.get('assigned_to_id')
        })
        return {'id': new_task.id}


