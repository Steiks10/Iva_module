from odoo import api, fields, models
from odoo.exceptions import UserError

class DateReportWizard(models.TransientModel):
    _name="covid_19.date.report.wizard"
    _description="Report between date and by country"

    start_date=fields.Date('Start Date', required=True)
    end_date=fields.Date('End Date', required=True)
    country_ids= fields.Many2many(
                                    "res.country",
                                    string="Countries",
                                    help="Countries you want to generate the report"
                                )

    def print_report(self):
        Covid19=self.env['covid.covid_19'] #instanciar el objeto donde va a buscar los datos
        domain=[
            ('date', '>=', self.start_date), #where 
            ('date', '<=', self.end_date)
        ]
        if self.country_ids:
            domain.append(('country_id', 'in', self.country_ids.ids)) #filtra por paises
        covidField=[
            'source',
            'date',
            'country_id',
            'infected',
            'recovered',
            ]    
        CovidRecords= Covid19.search_read(domain, covidField)
        data={
            'CovidRecords':CovidRecords,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'country_ids': self.country_ids,
            }
        return self.env.ref('covid-module.report_DateReportExternallayout').report_action(self, data=data) #pasa los datos
    

