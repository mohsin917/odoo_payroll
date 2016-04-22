# -*- coding: utf-8 -*-
from openerp import models, fields, api

class hr_payslip_run(models.Model):
    """
    Confirm all payslips in batch
    """
    _inherit = "hr.payslip.run"
    
    def confirm_payslips_in_batch(self, cr, uid, ids, context=None):
        
        # Get all payslips in this batch
        payslip_pool = self.pool.get('hr.payslip')
        payslip_ids = payslip_pool.search(cr, uid, [('payslip_run_id','=',ids), ('state', '=', 'draft') ], context=context)
        payslip_records = payslip_pool.browse(cr, uid, payslip_ids, context=context)
        
        for item in payslip_records:
            payslip_pool.hr_verify_sheet(cr, uid, item.id, context=context)
            payslip_pool.process_sheet(cr, uid, item.id, context=context)
        
        return True