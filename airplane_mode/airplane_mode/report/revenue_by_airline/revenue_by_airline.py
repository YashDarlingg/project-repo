# Copyright (c) 2023, Airplane and contributors
# For license information, please see license.txt

import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data

def execute(filters=None):
    columns, data = [
        {
            "label": "Airline",
            "fieldname": "airline",
            "fieldtype": "Link",
            "options": "Airline",
            "width":"150px"
        },
        {
            "label": "Revenue",
            "fieldname": "total_revenue",
            "fieldtype": "Currency",
            "width":"150px"
        },
    ], []

    records = frappe.db.sql(
        """
        SELECT `tabAirplane ticket`.Airline as airline, SUM(`tabAirplane ticket`.total_amount) as total_revenue
        FROM `tabAirplane ticket`
        WHERE `tabAirplane ticket`.docstatus = 1
        GROUP BY `tabAirplane ticket`.airline;
        """,
        as_dict=True,
    )

    revenue_by_airline = {}
    for record in records:
        if record.airline in revenue_by_airline:
            revenue_by_airline[record.airline] = revenue_by_airline[record.Airline] + record.total_amount
        else:
            revenue_by_airline[record.airline] = record.total_amount
    
    for airline, revenue in revenue_by_airline.items():
        data.append({"airline": airline, "revenue": revenue})

    return columns, records
