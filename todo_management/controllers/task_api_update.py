from odoo import http
from odoo.http import request, Response
import json

class TodoTaskAPIUpdate(http.Controller):

    @http.route('/api/tasks/<int:task_id>', auth='user', type='json', methods=['PUT'])
    def update_task(self, task_id, **kwargs):
        task_data = request.jsonrequest
        task = request.env['todo.task'].browse(task_id)
        if task.exists():
            task.write({
                'task_name': task_data.get('name', task.task_name),
                'description': task_data.get('description', task.description),
                'status': task_data.get('status', task.status)
            })
            return {'status': 'success'}
        return {'status': 'error', 'message': 'Task not found'}

