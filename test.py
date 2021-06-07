import unittest
from app import app


class FlaskTest(unittest.TestCase):

    def test_default(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status_code = response.status_code
        data = response.data.decode("utf-8")
        self.assertEquals(status_code, 200)
        self.assertEquals(data, '<form action=\"\" method=\"get\"><p>Nombre: <input type=\"text\" name=\"nombre\" size=\"40\"></p><p>Año de nacimiento: <input type=\"number\" name=\"nacido\" min=\"1900\"></p><p>Sexo:<input type=\"radio\" name=\"hm\" value=\"h\"> Hombre<input type=\"radio\" name=\"hm\" value=\"m\"> Mujer</p><p><input type=\"submit\" value=\"Enviar\"><input type=\"reset\" value=\"Borrar\"></p></form>')
        self.assertGreater(len(data),0)

if __name__ == '__main__':
    unittest.main()
