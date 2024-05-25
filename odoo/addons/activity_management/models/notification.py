from odoo import models, fields, api
from datetime import datetime, timedelta

class Notification(models.Model):
    _name = 'activity.management.notification'
    _description = 'Activity Notification'

    activity_id = fields.Many2one('activity.management.activity', string='Activity', required=True)
    notify_time = fields.Datetime(string='Notify Time')

    @api.model
    def create_notification(self, activity):
        notify_time = activity.start_date - timedelta(minutes=30)
        self.create({'activity_id': activity.id, 'notify_time': notify_time})

    @api.model
    def check_notifications(self):
        now = datetime.now()
        notifications = self.search([('notify_time', '<=', now)])
        for notification in notifications:
            # ส่งการแจ้งเตือนให้กับผู้ใช้
            notification.activity_id.message_post(body='Activity {} is starting soon.'.format(notification.activity_id.name))
            notification.unlink()
