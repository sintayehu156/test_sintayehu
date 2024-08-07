# Copyright (c) 2024, sintayehu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MonthlyTariffSummary(Document):
	
	# Calculates and sets tariff values based on power consumption data before saving the document.
	def before_save(self):
		data_records = self.get_power_consumption_data(self.customer, self.year, self.month)
		
		low_tariff_kwh_total, high_tariff_kwh_total, low_tariff_count, high_tariff_count = self.calculate_tariff_totals(data_records)
		
		self.average_kwh_in_a_high_tariff_period = self.calculate_average(high_tariff_kwh_total, high_tariff_count)
		self.average_kwh_in_a_low_tariff_period = self.calculate_average(low_tariff_kwh_total, low_tariff_count)
		
		self.low_tariff = 0.1 * self.average_kwh_in_a_low_tariff_period
		self.high_tariff = 0.3 * self.average_kwh_in_a_high_tariff_period

    # Fetches power consumption data from 'Power Consumption Data' Doctype.
	def get_power_consumption_data(self, customer, year, month):
		return frappe.get_all(
			'Power Consumption Data',
			filters={
				'customer': customer,
				'year': year,
				'month': month,
				'consumption_type': 'KWH'
			},
			fields=['tariff_period', 'power_consumption']
		)
    # Calculates total kWh and count for low and high tariff periods.
	def calculate_tariff_totals(self, data_records):
		low_tariff_kwh_total = 0
		high_tariff_kwh_total = 0
		low_tariff_count = 0
		high_tariff_count = 0
		
		for record in data_records:
			if record['tariff_period'] == 'Low':
				low_tariff_kwh_total += record['power_consumption']
				low_tariff_count += 1
			elif record['tariff_period'] == 'High':
				high_tariff_kwh_total += record['power_consumption']
				high_tariff_count += 1
		
		return low_tariff_kwh_total, high_tariff_kwh_total, low_tariff_count, high_tariff_count
	
    # Computes the average kWh based on total kWh and count.
	def calculate_average(self, total_kwh, count):
		return total_kwh / count if count > 0 else 0
