from django.test import TestCase


class TestDraculaAdmin(TestCase):
    def test_theme_loaded(self):
        """
        On the admin login page, check that the rendered
        template contains the updated dark theme toggle icon (bat),
        and not the old one (moon).

        The bat icon is the only HTML change this package makes to the admin,
        everything else comprises of static file changes (CSS and SVG).
        """

        # Act
        response = self.client.get("/admin", follow=True)

        response_content = response.content.decode("utf-8")

        # Assert
        self.assertTrue("icon-bat" in response_content)
        self.assertFalse("icon-moon" in response_content)
        self.assertEqual(response.status_code, 200)
