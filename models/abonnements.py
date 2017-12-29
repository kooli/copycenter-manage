# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Abonnement(models.Model):
    _name           = 'copycenter_uniflex.abonnement'
    _description    = 'Represente les cartes prepayees des clients'

    client_id       = fields.Many2one('res.partner', 'Client')

    codebar         = fields.Char(string="Code Bar", required=True)
    date_adonnement = fields.Datetime("Date d'abonnement")
    solde           = fields.Float("Solde", (9, 2))
    decouvert       = fields.Boolean("A un découvert ?")
    plafond_decouvert = fields.Float("Plafond du découvert", (9, 2))
    status          = fields.Boolean("Activé ?")
    desc            = fields.Text("Note supplémentaire")



class TypeAbonnement(models.Model):
    _name           = "copycenter_uniflex.type_abonnement"
    _description    = "Represente les types d'abonnement ou de carte"

    nom             = fields.Char("Type d'abonnement", required=True)
    desc            = fields.Text("Note supplémentaire")