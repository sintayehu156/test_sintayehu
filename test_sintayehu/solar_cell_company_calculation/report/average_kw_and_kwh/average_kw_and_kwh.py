# Copyright (c) 2024, sintayehu and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    
    return columns, data

def get_columns():
    return [
        {
            "label": "Customer",
            "fieldname": "customer_name",
            "fieldtype": "Link",
            "options": "Customer",
            "width": 200
        },
        {
            "label": "Average KWH",
            "fieldname": "avg_kwh",
            "fieldtype": "Float",
            "width": 150
        },
        {
            "label": "Average KW",
            "fieldname": "avg_kw",
            "fieldtype": "Float",
            "width": 150
        }
    ]

def get_data(filters):
    customer_filter = ""
    
    # Apply customer filter if provided
    if filters.get('customer'):
        customer_filter = "AND pc.customer = %(customer)s"
    
    return frappe.db.sql(f"""
        SELECT
            pc.customer AS customer_name,
            AVG(CASE WHEN pc.consumption_type = 'KWH' THEN pc.power_consumption ELSE NULL END) AS avg_kwh,
            AVG(CASE WHEN pc.consumption_type = 'KW' THEN pc.power_consumption ELSE NULL END) AS avg_kw
        FROM
            `tabPower Consumption Data` pc
        WHERE
            1 = 1 {customer_filter}
        GROUP BY
            pc.customer
    """, filters, as_dict=True)
