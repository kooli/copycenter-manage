# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Transaction(models.Model):
    _name           = 'copycenter_uniflex.transaction'
    _description    = 'Represente les differentes transactions du client'

    abonnement_id           = fields.Many2one('res.partner', 'Abonnement')
    type_transsaction_id    = fields.Many2one("copycenter_uniflex.type_transaction", "Type de transaction", required=True)

    montant         = fields.Float("Montant", (9, 2))
    date_transaction = fields.Datetime("Date de la transaction")
    last_solde      = fields.Float("Ancien Solde", (9, 2))
    new_solde       = fields.Float("Nouveau Solde", (9, 2))
    desc            = fields.Text("Note Supplémentaire")



class TypeTransaction(models.Model):
    _name           = 'copycenter_uniflex.type_transaction'
    _description    = 'Represente les type de transactions'

    nom             = fields.Char("Type de transaction", required=True)
    desc            = fields.Text("Note Supplémentaire")