from odoo import http
from odoo.http import request


class TodoTaskAPIDelete(http.Controller):

    @http.route('/api/tasks/<int:task_id>', auth='user', type='json', methods=['DELETE'])
    def delete_task(self, task_id, **kwargs):
        task = request.env['todo.task'].browse(task_id)
        if task.exists():
            task.unlink()
            return {'status': 'success'}
        return {'status': 'error', 'message': 'Task not found'}

