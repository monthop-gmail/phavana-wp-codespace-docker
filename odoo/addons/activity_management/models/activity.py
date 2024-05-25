from odoo import models, fields, api

class Activity(models.Model):
    _name = 'activity.management.activity'
    _description = 'Activity'

    name = fields.Char(string='Activity Name', required=True)
    start_date = fields.Datetime(string='Start Date', required=True)
    end_date = fields.Datetime(string='End Date', required=True)
    activity_type = fields.Selection([
        ('daily', 'Daily'),
        ('special_day', 'Special Day'),
        ('special_period', 'Special Period')
    ], string='Activity Type', required=True, default='daily')
    interval_hours = fields.Integer(string='Interval Hours', default=0, help="Minimum hours between rounds for special period activities")
    visible = fields.Boolean(string='Visible', default=False)
    sub_activity_ids = fields.One2many('activity.management.sub_activity', 'activity_id', string='Sub Activities')

    @api.model
    def create(self, vals):
        record = super(Activity, self).create(vals)
        self.env['activity.management.notification'].create_notification(record)
        return record

    def action_set_visible(self):
        self.visible = True

    def action_set_invisible(self):
        self.visible = False

class SubActivity(models.Model):
    _name = 'activity.management.sub_activity'
    _description = 'Sub Activity'

    name = fields.Char(string='Sub Activity Name', required=True)
    duration = fields.Integer(string='Duration (Minutes)', required=True)
    points = fields.Integer(string='Points', required=True)
    activity_id = fields.Many2one('activity.management.activity', string='Activity', required=True)
    completed = fields.Boolean(string='Completed', default=False)
    user_id = fields.Many2one('res.users', string='Participant')

    # @api.multi
    def complete_activity(self):
        for sub_activity in self:
            sub_activity.completed = True
            sub_activity.user_id.points += sub_activity.points
            if not sub_activity.activity_id.sub_activity_ids.filtered(lambda x: not x.completed):
                sub_activity.user_id.points += sub_activity.activity_id.special_points

class User(models.Model):
    _inherit = 'res.users'

    points = fields.Integer(string='Points', default=0)
