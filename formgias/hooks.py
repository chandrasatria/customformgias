# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "formgias"
app_title = "formgias"
app_publisher = "Frappe"
app_description = "App for form in gias"
app_icon = "octicon octicon-book"
app_color = "#589494"
app_email = "info@frappe.io"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/formgias/css/formgias.css"
# app_include_js = "/assets/formgias/js/formgias.js"

# include js, css files in header of web template
# web_include_css = "/assets/formgias/css/formgias.css"
# web_include_js = "/assets/formgias/js/formgias.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "formgias.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "formgias.install.before_install"
# after_install = "formgias.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "formgias.notifications.get_notification_config"

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
# 		"formgias.tasks.all"
# 	],
# 	"daily": [
# 		"formgias.tasks.daily"
# 	],
# 	"hourly": [
# 		"formgias.tasks.hourly"
# 	],
# 	"weekly": [
# 		"formgias.tasks.weekly"
# 	]
# 	"monthly": [
# 		"formgias.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "formgias.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "formgias.event.get_events"
# }

