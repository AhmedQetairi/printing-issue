# -*- coding: utf-8 -*-
{
    'name': 'Report Options - Download, View, Print',
    'version': '14.0.1.0.0',
    'license': 'LGPL-3',
    'summary': """shows a modal window with options for printing, downloading or opening pdf reports""",
    'description': """
        Choose one of the following options when printing a pdf report:
        - print. print the pdf report directly with the browser
        - download. download the pdf report on your computer
        - open. open the pdf report in a new tab
        You can also set a default options for each report
    """,
    'author': 'Luis Rodrigo Mejia Mateus, Odoo Mates',
    # 'live_test_url': 'https://www.youtube.com/watch?v=-34_UxtFMO0',
    'category': 'Productivity',
    'images': ['images/main_1.png',
               'images/main_screenshot.png'
               ],
    'depends': ['base','web'],
    'data': [
        # 'views/templates.xml',
        'views/ir_actions_report.xml',
    ],
    
    'assets': {
        'web.assets_backend': [
            
            "/om_report_pdf_options/static/src/js/pdf_options.js",
            "/om_report_pdf_options/static/src/js/qwebactionmanager.js",
        ],
        
        'web.assets_qweb':[
            "/om_report_pdf_options/static/src/xml/report_pdf_options.xml",
        ]
    },
    
    "external_dependencies": {"python": ["dateutil"]},
    'installable': True,
    'auto_install': False,
}
