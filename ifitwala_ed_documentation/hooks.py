# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ifitwala_ed_documentation"
app_title = "Ifitwala Ed Documentation"
app_publisher = "Ifitwala"
app_description = "Documentation for the Frappe app Ifitwala Education. A K-12 School management system centered on analytics. "
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "f.deryckel@gmail.com"
app_license = "MIT"

website_context = {
	"repo": "fderyckel/ifitwala_ed_documentation",
	"hide_login": 1,
	"favicon": "/assets/ifitwala_ed_documentation/img/erpnext-logo-blue.png"
}


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ifitwala_ed_documentation/css/ifitwala_ed_documentation.css"
# app_include_js = "/assets/ifitwala_ed_documentation/js/ifitwala_ed_documentation.js"

# include js, css files in header of web template
# web_include_css = "/assets/ifitwala_ed_documentation/css/ifitwala_ed_documentation.css"
# web_include_js = "/assets/ifitwala_ed_documentation/js/ifitwala_ed_documentation.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ifitwala_ed_documentation/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "index"

base_template_map = {
	r'docs/user/manual.*': 'templates/ifitwala_ed_docs.html'
}

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ifitwala_ed_documentation.install.before_install"
# after_install = "ifitwala_ed_documentation.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ifitwala_ed_documentation.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ifitwala_ed_documentation.tasks.all"
# 	],
# 	"daily": [
# 		"ifitwala_ed_documentation.tasks.daily"
# 	],
# 	"hourly": [
# 		"ifitwala_ed_documentation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ifitwala_ed_documentation.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ifitwala_ed_documentation.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ifitwala_ed_documentation.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ifitwala_ed_documentation.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ifitwala_ed_documentation.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]
