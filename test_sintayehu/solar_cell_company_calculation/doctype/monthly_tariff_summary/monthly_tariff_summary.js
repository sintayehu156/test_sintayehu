// Copyright (c) 2024, sintayehu and contributors
// For license information, please see license.txt

frappe.ui.form.on("Monthly Tariff Summary", {
	refresh(frm) {
		// current date
		let today = new Date();

		// Extract the current year and month
		let year = today.getFullYear();
		let month = today.toLocaleString("default", { month: "long" });
                
		// Set the 'year' and 'month' fields in the form
		frm.set_value("year", year);
		frm.set_value("month", month);
	},
});
