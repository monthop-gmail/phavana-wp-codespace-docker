{
    'name': 'Activity Management',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Manage online activities with points system',
    'description': 'A module to manage online activities and reward points to participants.',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'views/activity_views.xml',
        'views/sub_activity_views.xml',
        'security/ir.model.access.csv',
        'data/cron_jobs.xml',
    ],
    'demo': [
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
}
