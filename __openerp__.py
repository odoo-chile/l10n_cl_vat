# -*- encoding: utf-8 -*-
##############################################################################
#
# Odoo / OpenERP, Open Source Management Solution
# By Blanco Martín & Asociados - (http://blancomartin.cl).
#
#
#
# Original from Cubic ERP - Teradata SAC. (http://cubicerp.com).
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

{
    'name': 'Base VAT CL - To check Chilean VAT (RUT) number validity',
    'version': '1.1',
    'category': 'Generic Modules/Base',
    'description': """
Chilean VAT (RUT) Validator
===========================

This validator is a fork from https://github.com/CubicERP/odoo/tree/master/extra-addons/l10n_cl_vat

The cause we decided to make this fork avalable to public, is because althought we detected a bug at original developement, and contributed the change to solve it thru a pull request has not been accepted yet.

So this fork will allow people using OpenERP or Odoo to update the module with this one, which solves the bug.

The bug is very simple: VATs (or RUTs) with verification digit = 0, will not validate with the original developement.

The change we made is minimum, but is a critical situation if you can't save a Partner profile without the correct VAT.

To apply:

1) Copy l10n_cl_vat directory into "addons" directory of your Odoo/OpenERP instance.
2) Refresh module list.
3) Install or re-install the module as usual.
""",
    'author': 'Blanco Martín & Asociados',
    'depends': ['base_vat'],
    'website': 'http://blancomartin.cl',
    'license': 'AGPL-3',
    'installable': True,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
