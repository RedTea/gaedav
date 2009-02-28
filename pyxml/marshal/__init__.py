"""Converting Python objects to XML and back again.

pyxml.marshal.generic
  Marshals simple Python data types into a custom XML format.  The
  Marshaller and Unmarshaller classes can be subclassed in order to
  implement marshalling into a different XML DTD.

pyxml.marshal.wddx
  Marshals Python data types into the WDDX DTD.
"""

__all__ = ['generic', 'wddx']
