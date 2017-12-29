# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Client(models.Model):
    # _name = 'copycenter_uniflex.client'
    # _description = "Represente tous les clients du CopyCenter"
    _inherit = 'res.partner'
    # nom = fields.Char(string="Nom", required=True)
    # prenom = fields.Char(string="Prenom")
    # matricule = fields.Char(string="Matricule")
    # photo = fields.Char(string="Photo")
    # niveau = fields.Char(string="Niveau")
    type_client = fields.Selection(selection=[('etudiant', 'Étudiant'), ('enseignant', 'Enseignant'), ('etablissement', 'Établissement')],
                                   default='etudiant', required=True)