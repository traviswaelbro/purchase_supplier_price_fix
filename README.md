# Supplier Purchase Price Fix

_purchase_supplier_price_fix_ is a fix to a minor bug, which we encountered with the base _purchase_ module. 

If a product had a Supplier set, but the supplier did not have a Qty & Unit Price set, then the price would be set to $0.00 when a RFQ/PO was created under that supplier.

This module simply adds a fallback to the default cost price of the product.

##### To Do:

- Test in default instance
- Rewrite model with _super()_ to inherit the default method instead of overwriting it
- Rewrite in v8 API?
