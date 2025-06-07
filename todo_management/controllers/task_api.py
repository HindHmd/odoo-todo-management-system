from odoo import http
from odoo.http import request, Response
import json

class TodoTaskAPI(http.Controller):

    @http.route('/api/tasks', auth='user', type='http', methods=['GET'])
    def get_tasks(self, **kwargs):
        tasks = request.env['todo.task'].search([])
        task_list = []
        for task in tasks:
            task_list.append({
                'id': task.id,
                'name': task.task_name,
                'description': task.description,
                'status': task.status,
                'assigned_to': task.assign_to_id.name
            })
        return Response(json.dumps(task_list), headers={'Content-Type': 'application/json'})


