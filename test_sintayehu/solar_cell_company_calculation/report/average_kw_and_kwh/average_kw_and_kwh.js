// Copyright (c) 2024, sintayehu and contributors
// For license information, please see license.txt

frappe.query_reports["Average KW and KWH"] = {
	"filters": [
        {
            fieldname: "customer",
            label: __("Customer"),
            fieldtype: "Link",
            options: "Customer"
        },
    ]
};
