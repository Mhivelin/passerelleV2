import unittest
from app import create_app
from app.models.ebp import EBP


class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    # def test_ebp(self):
    #     ebp = EBP(1)
    #     ebp.BdGetClientEBP(1)
    #     ebp.login()

    #     self.assertIsNotNone(ebp)

    def test_get_folders(self):
        ebp = EBP(1)
        ebp.BdGetClientEBP(1)
        ebp.login()

        folders = ebp.get_folders()
        print(folders)

        self.assertIsNotNone(folders)

    # def test_Bdtoken_saver(self):
    #     ebp = EBP(1)

    #     ebp.Bdtoken_saver('token')
    #     print(ebp.BdGetClientEBP(1))

    # def test_Bdtoken_clear(self):
    #     ebp = EBP(1)

    #     ebp.Bdtoken_clear()
    #     print(ebp.BdGetClientEBP(1))

    def getSupplier(self):
        ebp = EBP(1)
        ebp.BdGetClientEBP(1)
        ebp.login()

        suppliers = ebp.get_suppliers()
        print(suppliers)

        self.assertIsNotNone(suppliers)


if __name__ == '__main__':
    unittest.main()
