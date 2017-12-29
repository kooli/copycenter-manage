# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Imprimante(models.Model):
    _name           = 'copycenter_uniflex.imprimante'
    _description    = 'Imprimante utilisé dans le Copy Center'
    _rec_name       = 'nom'


    nom             = fields.Char("Nom de l'équipement", required=True)
    model           = fields.Text("Modèle")
    sn              = fields.Text("Numéro de Série")


class EtatImprimante(models.Model):
    _name           = 'copycenter_uniflex.etat_imprimante'
    _description    = 'Represente le statut de l\'imprimante a moment T'

    copie_nb        = fields.Integer('Nombre de copies Noir&Blanc')
    copie_couleur   = fields.Integer('Nombre de copies Couleures')
    toner_noir      = fields.Integer('Toner Noir')
    toner_cyan      = fields.Integer('Toner Cyan')
    toner_magenta   = fields.Integer('Toner Magenta')
    toner_jaune     = fields.Integer('Toner Jaune')
    tambour_couleur = fields.Integer('Tambour Couleur')
    tambour_magenta = fields.Integer('Tambour Magenta')
    tambour_jaune   = fields.Integer('Tambour Jaune')
    fr_toner        = fields.Integer('Flacon récupérateur de Toner')
    r_transfert     = fields.Integer('Rouleau de 2ème Transfert')
    
    imprimante_id   = fields.Many2one("copycenter_uniflex.imprimante", "Imprimante", required=True)
