import unittest
from higiene.models import Producto


class testAlumno(unittest.TestCase):

    def test_crear_objeto(self):
        producto = Producto.objects.create(
                                       id_producto='5',
                                       nombre='Lysol',
                                       precio='990',
                                       fecha_env='Oct. 20, 2020',
                                       marca='Lysol'
                                       )
        producto.save()

        self.assertTrue(producto,True)

    def test_val_id(self):
        producto = Producto.objects.get(id_producto='5')
        self.assertEquals(producto.id_producto, '5')
