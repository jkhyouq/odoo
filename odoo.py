import xmlrpc.client
class OdooIntegration:
    def __int__(self, odoo_url, odoo_db, odoo_username, odoo_password):
        self.odoo_url = odoo_url
        self.odoo_db = odoo_db
        self.odoo_username = odoo_username
        self.odoo_password = odoo_password
        self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(odoo_url))
        self.uid = self.common.authentificate(odoo_db, odoo_username, odoo_password,{})
        self.models = xmlrpc.client.ServerProxy('{}xmlrpc/2/object'.format(odoo_url))

    def create_marked_products(self, product_name, quantity):
        pass

    def update_product_properties(self, product_id, new_warehouse, new_status):
        pass

    def add_expenses_entry(self, product_id, expense_category, amount, date):
        pass




