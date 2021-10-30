# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class esidons(models.Model):
#     _name = 'esidons.openacademy'

#     name = fields.Char()
class Campagne(models.Model):
    _name = 'esidons.campagne'
    _description = "Description"
    _motif='Motif'
    _beneficiaire='Bénéficiaires'
    _typedon='Type de dons'
    _datedeb='Date début'
    _datefin='Date fin'
    _suffisant='Dons suffisants'
    _active='Compagne archive'
    datedeb=fields.Date(required=True)
    datefin=fields.Date(required=True)

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    motif = fields.Char(string="Motif",required=True)
    beneficiaire = fields.Char(string="Bénéficiaires visés", required=True)
    typedon = fields.Char(string="Type dons", required=True)
    suffisant=fields.Boolean(default=False)
    active=fields.Boolean("Active",default=True)
    benif_ids = fields.Many2many(
        'esidons.benif', 'campagne_id', string="Bénéficiaires")
    don_ids = fields.One2many(
        'esidons.don', 'campagne_id',string="Donateurs")

class Benif(models.Model):
    _name = 'esidons.benif'
    _adresse = "Adresse"
    _age = "age donateur"
    _tel="Numéro de téléphone"
    name = fields.Char(required=True)
    adresse = fields.Text(required=True)
    age = fields.Integer(string="Age")
    tel=fields.Text()
    campagne_id = fields.Many2many('esidons.campagne','benif_ids', string="Campagne", required=True)
class Don(models.Model):
    _name = 'esidons.don'
    _typededon = "Type de dons"
    _age = "Age donateur"
    _anon="Anonyme"
    anon=fields.Boolean(default=False)
    name = fields.Char()
    typededon = fields.Text(required=True)
    age = fields.Integer(string="Age")
    campagne_id = fields.Many2one('esidons.campagne', ondelete='cascade', string="Campagne", required=True)
