l10n_cl_vat
===========

Chilean VAT (RUT) Validator
===========================

This validator is a fork from https://github.com/CubicERP/odoo/tree/master/extra-addons/l10n_cl_vat

The cause we decided to make this fork avalable to public, is because althought we detected a bug at original developement, and contributed the change to solve it, thru a pull request, the owner of the original branch
(CubicERP) did not accepted it yet.

So this fork will allow people using OpenERP or Odoo to update the module with this one, which solves the bug.

The bug is very simple: VATs (or RUTs) with verification digit = 0, will not validate with the original developement.

The change we made is minimum, but is a critical situation if you can't save a Partner profile without the correct VAT.

To apply:

1) Copy l10n_cl_vat directory into "addons" directory of your Odoo/OpenERP instance.
2) Refresh module list.
3) Install or re-install the module as usual.


Validator de VAT para Chile
===========================

Este validador es un desprendimiento del desarrollo original, que Ud. encontrará en https://github.com/CubicERP/odoo/tree/master/extra-addons/l10n_cl_vat

La causa por la cual decidimos poner este desarrollo disponible al público en forma explícita, es porque, aunque nosotros detectamos la falla sobre el desarrollo original, y contribuimos el cambio para resolverlo a través de una solicitud de unión del desarrollo (pull request), el propietario del desarrolloo original CubicERP no aceptó el cambio todavía.

Por lo tanto, este desarrollo permitirá a empresas, usuarios o implmenetadores actualizar el módulo y de esta manera resolver el error prontamente.

El bug es muy simple: VATs (o RUTs) con dígito verificador = 0 no validarán en el desarrollo original.

El cambio que hicimos es mínimo, pero es una situación crítica si no puedes guardar un cliente o proveedor (partner) en tu base de datos por la falta del RUT.

To aplicar el desarrollo:

1) Copia el directorio l10n_cl_vat dentro del directorio "addons" de tu instancia Odoo/OpenERP.
2) Actualiza la lista de módulos.
3) Instala o reinstala el módulo como se hace usualmente.

