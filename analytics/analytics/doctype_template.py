def get_analytics_doctype_name(doctype):
    return (doctype + " Field History")

def get_change_doctype_json(doctype):
    return {
         "allow_copy": 0,
         "allow_import": 0,
         "allow_rename": 0,
         "creation": "2016-04-17 16:18:44.523847",
         "custom": 0,
         "docstatus": 0,
         "doctype": "DocType",
         "document_type": "Document",
         "fields": [
          {
           "allow_on_submit": 0,
           "bold": 0,
           "collapsible": 0,
           "fieldname": "changed_doc_name",
           "fieldtype": "Data",
           "hidden": 0,
           "ignore_user_permissions": 0,
           "ignore_xss_filter": 0,
           "in_filter": 0,
           "in_list_view": 0,
           "label": "Document Name",
           "length": 0,
           "no_copy": 0,
           "permlevel": 0,
           "precision": "",
           "print_hide": 0,
           "print_hide_if_no_value": 0,
           "read_only": 1,
           "report_hide": 0,
           "reqd": 0,
           "search_index": 0,
           "set_only_once": 0,
           "unique": 0
          },
          {
           "allow_on_submit": 0,
           "bold": 0,
           "collapsible": 0,
           "fieldname": "date",
           "fieldtype": "Datetime",
           "hidden": 0,
           "ignore_user_permissions": 0,
           "ignore_xss_filter": 0,
           "in_filter": 0,
           "in_list_view": 0,
           "label": "Date",
           "length": 0,
           "no_copy": 0,
           "permlevel": 0,
           "precision": "",
           "print_hide": 0,
           "print_hide_if_no_value": 0,
           "read_only": 1,
           "report_hide": 0,
           "reqd": 0,
           "search_index": 0,
           "set_only_once": 0,
           "unique": 0
          },
          {
           "allow_on_submit": 0,
           "bold": 0,
           "collapsible": 0,
           "fieldname": "modified_by_user",
           "fieldtype": "Data",
           "hidden": 0,
           "ignore_user_permissions": 0,
           "ignore_xss_filter": 0,
           "in_filter": 0,
           "in_list_view": 0,
           "label": "Modified By User",
           "length": 0,
           "no_copy": 0,
           "permlevel": 0,
           "precision": "",
           "print_hide": 0,
           "print_hide_if_no_value": 0,
           "read_only": 1,
           "report_hide": 0,
           "reqd": 0,
           "search_index": 0,
           "set_only_once": 0,
           "unique": 0
          },
          {
           "allow_on_submit": 0,
           "bold": 0,
           "collapsible": 0,
           "fieldname": "fieldname",
           "fieldtype": "Data",
           "hidden": 0,
           "ignore_user_permissions": 0,
           "ignore_xss_filter": 0,
           "in_filter": 0,
           "in_list_view": 0,
           "label": "Fieldname",
           "length": 0,
           "no_copy": 0,
           "permlevel": 0,
           "precision": "",
           "print_hide": 0,
           "print_hide_if_no_value": 0,
           "read_only": 1,
           "report_hide": 0,
           "reqd": 0,
           "search_index": 0,
           "set_only_once": 0,
           "unique": 0
          },
          {
           "allow_on_submit": 0,
           "bold": 0,
           "collapsible": 0,
           "fieldname": "old_value",
           "fieldtype": "Data",
           "hidden": 0,
           "ignore_user_permissions": 0,
           "ignore_xss_filter": 0,
           "in_filter": 0,
           "in_list_view": 0,
           "label": "Old Value",
           "length": 0,
           "no_copy": 0,
           "permlevel": 0,
           "precision": "",
           "print_hide": 0,
           "print_hide_if_no_value": 0,
           "read_only": 1,
           "report_hide": 0,
           "reqd": 0,
           "search_index": 0,
           "set_only_once": 0,
           "unique": 0
          },
          {
           "allow_on_submit": 0,
           "bold": 0,
           "collapsible": 0,
           "fieldname": "new_value",
           "fieldtype": "Data",
           "hidden": 0,
           "ignore_user_permissions": 0,
           "ignore_xss_filter": 0,
           "in_filter": 0,
           "in_list_view": 0,
           "label": "New Value",
           "length": 0,
           "no_copy": 0,
           "permlevel": 0,
           "precision": "",
           "print_hide": 0,
           "print_hide_if_no_value": 0,
           "read_only": 1,
           "report_hide": 0,
           "reqd": 0,
           "search_index": 0,
           "set_only_once": 0,
           "unique": 0
          }
         ],
         "hide_heading": 0,
         "hide_toolbar": 0,
         "idx": 0,
         "in_create": 0,
         "in_dialog": 0,
         "is_submittable": 0,
         "issingle": 0,
         "istable": 0,
         "max_attachments": 0,
         "modified": "2016-04-19 19:33:53.699191",
         "modified_by": "Administrator",
         "module": "Analytics",
         "name": doctype,
         "name_case": "",
         "owner": "Administrator",
         "permissions": [
          {
           "amend": 0,
           "apply_user_permissions": 0,
           "cancel": 0,
           "create": 1,
           "delete": 1,
           "email": 1,
           "export": 1,
           "if_owner": 0,
           "import": 0,
           "permlevel": 0,
           "print": 1,
           "read": 1,
           "report": 1,
           "role": "Administrator",
           "set_user_permissions": 0,
           "share": 1,
           "submit": 0,
           "write": 1
          }
         ],
         "read_only": 0,
         "read_only_onload": 0,
         "sort_field": "modified",
         "sort_order": "DESC"
        }
