from . import models
from odoo import api, SUPERUSER_ID

def _auto_check_notifications(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['activity.management.notification'].check_notifications()