// Copyright (c) 2024, sintayehu and contributors
// For license information, please see license.txt

frappe.ui.form.on('Power Consumption Data', {
    refresh(frm) {
        let today = new Date();
        let year = today.getFullYear();
        let month = today.toLocaleString('default', { month: 'long' });
    
        frm.set_value('year', year);
        frm.set_value('month', month);

	},
    timestamp: function(frm) {
        if (frm.doc.timestamp) {
            // Extract hours and minutes from the Time type field
            let timeString = frm.doc.timestamp;
            let [hours, minutes] = timeString.split(':').map(Number);

            // Determine the tariff period
            let tariffPeriod;

            if (hours >= 23 || hours < 6) {
                // Low tariff period: 11:00 PM to 5:59 AM
                tariffPeriod = 'Low';
            } else {
                // High tariff period: 6:00 AM to 10:59 PM
                tariffPeriod = 'High';
            }

            frm.set_value('tariff_period', tariffPeriod);
        }
    }

});


