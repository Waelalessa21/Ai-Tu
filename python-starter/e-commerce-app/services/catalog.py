from models.product import Product


class ProductCatalog:
    def __init__(self, storage):
        self.storage = storage

    def get_all(self):
        return [Product.from_dict(item) for item in self.storage.get_all()]

    def get_by_id(self, product_id):
        data = self.storage.get_by_id(product_id)
        if data:
            return Product.from_dict(data)
        return None

    def add_product(self, product):
        self.storage.create(product.to_dict())
