# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "patanjali"
app_title = "Patanjali"
app_publisher = "indictrans"
app_description = "sales order UOM amount calculation and print format"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "pooja.s@indictranstech.com"
app_license = "indictrans"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/patanjali/css/patanjali.css"
# app_include_js = "/assets/patanjali/js/patanjali.js"

# include js, css files in header of web template
# web_include_css = "/assets/patanjali/css/patanjali.css"
# web_include_js = "/assets/patanjali/js/patanjali.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------
fixtures = ["Custom Field", "Property Setter", "Print Format", "Report", "Custom Script","Letter Head"]

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "patanjali.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "patanjali.install.before_install"
# after_install = "patanjali.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "patanjali.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }
doctype_js={
	"Sales Order":"patanjali/custom_script/sales_order/sales_order.js",
	"Sales Invoice":"patanjali/custom_script/sales_invoice/sales_invoice.js",
	"Delivery Note":"patanjali/custom_script/delivery_note/delivery_note.js",
	"Batch":"patanjali/custom_script/batch/batch.js"
}
# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Invoice": {
		"validate": "patanjali.patanjali.custom_script.sales_invoice.sales_invoice.calculate_qty"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"patanjali.tasks.all"
# 	],
# 	"daily": [
# 		"patanjali.tasks.daily"
# 	],
# 	"hourly": [
# 		"patanjali.tasks.hourly"
# 	],
# 	"weekly": [
# 		"patanjali.tasks.weekly"
# 	]
# 	"monthly": [
# 		"patanjali.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "patanjali.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "patanjali.event.get_events"
# }

