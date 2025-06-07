{
    'name': "To Do",
    'author': "hind",
    'version': "16.0.0.4.0",
    'category': "",
    'depends': ['base' , 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/base_menu.xml' ,
        'views/todo_view.xml' ,
        'views/tasker_view.xml',
        'reports/todo_report.xml' ,
        'wizard/ task_assignment_wizard_view.xml',


    ],
    'external_dependencies': {
        'python': ['json'],
    },

    'application': True,
}