# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    'name': 'Travel Agency Fees',
    'version': '11.0.1.0.0',
    'license': 'LGPL-3',
    'category': 'Uncategorized',
    "sequence": 3,
    'summary': 'Manage Fees',
    'complexity': "easy",
    'author': 'Xsellence Bangladesh Limited',
    'website': '"http://www.xsellencebdltd.com"',
    'depends': ['travel__agency', 'account_invoicing'],
    'data': [
        
        'views/student_view.xml',
        'views/umrah_view.xml',
        'views/guide_view.xml',
        'views/um_guide.xml',
        
    ],
    'images': [
        'static/description/openeducat_fees_banner.jpg',
    ],
    'demo': [
       
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
