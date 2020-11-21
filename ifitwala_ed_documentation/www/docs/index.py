# -*- coding: utf-8 -*-
# Copyright (c) 2020, ifitwala and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def get_context(context):
    frappe.flags.redirect_location = "/"
    raise frappe.Redirect
