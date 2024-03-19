import unittest
from app import create_app
from app.models.zeendoc import Zeendoc


class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_zeendoc(self):
        zeendoc = Zeendoc(1)
        zeendoc.BdGetClientZeendoc(1)
        zeendoc.login()

        # print(zeendoc.getright()['Collections'])
        self.assertIsNotNone(zeendoc.getright())

        self.assertIsNotNone(zeendoc)

    def test_get_classeurs(self):
        zeendoc = Zeendoc(1)
        zeendoc.BdGetClientZeendoc(1)
        zeendoc.login()

        self.assertIsNotNone(zeendoc.get_classeurs())


if __name__ == '__main__':
    unittest.main()
