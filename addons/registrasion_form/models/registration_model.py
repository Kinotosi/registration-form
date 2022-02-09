from odoo import api, fields, models, _

class RegistrationForm(models.Model):
    _name = "registration.form"
    _description = "Registration Form"

    name = fields.Char('Fullname', readonly=True)
    firtsname = fields.Char('Firtsname', required=True) 
    lastname = fields.Char('Lastname', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', required=True)  
    address = fields.Text('Address')

    @api.model
    def create(self, vals):
        res = super(RegistrationForm, self).create(vals)
        res.update({'name': "{} {}".format(res.firtsname, res.lastname)})
        return res

    def write(self, vals):
        if vals.get('firtsname') and vals.get('lastname'):
            vals.update({'name': "{} {}".format(vals.get('firtsname'), vals.get('lastname'))})
        elif vals.get('firtsname'):
            vals.update({'name': "{} {}".format(vals.get('firtsname'), self.lastname)})
        elif vals.get('lastname'):
            vals.update({'name': "{} {}".format(self.firtsname, vals.get('lastname'))})
        return super(RegistrationForm, self).write(vals)
