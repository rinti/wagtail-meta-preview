from wagtail.admin.staticfiles import versioned_static
from django.utils.html import format_html

from wagtail.core import hooks


@hooks.register("insert_global_admin_css", order=100)
def global_admin_css():
    """Add /static/css/custom.css to the admin."""
    return format_html(
        '<link rel="stylesheet" href="{}">',
        versioned_static("wagtail_seo_preview/static/admin.css"),
    )


@hooks.register("insert_global_admin_js", order=100)
def global_admin_js():
    """Add /static/css/custom.js to the admin."""
    return format_html(
        '<script src="{}"></script>',
        versioned_static("wagtail_seo_preview/static/admin.js"),
    )
