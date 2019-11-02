from django.core.management.base import BaseCommand

from mind_core.compat import coreapi
from mind_core.renderers import (
    CoreJSONRenderer, JSONOpenAPIRenderer, OpenAPIRenderer
)
from mind_core.schemas.generators import SchemaGenerator


class Command(BaseCommand):
    help = "Generates configured API schema for project."

    def add_arguments(self, parser):
        parser.add_argument('--title', dest="title", default=None, type=str)
        parser.add_argument('--url', dest="url", default=None, type=str)
        parser.add_argument('--description', dest="description", default=None, type=str)
        parser.add_argument('--format', dest="format", choices=['openapi', 'openapi-json', 'corejson'], default='openapi', type=str)

    def handle(self, *args, **options):
        assert coreapi is not None, 'coreapi must be installed.'

        generator = SchemaGenerator(
            url=options['url'],
            title=options['title'],
            description=options['description']
        )

        schema = generator.get_schema(request=None, public=True)

        renderer = self.get_renderer(options['format'])
        output = renderer.render(schema, renderer_context={})
        self.stdout.write(output.decode('utf-8'))

    def get_renderer(self, format):
        renderer_cls = {
            'corejson': CoreJSONRenderer,
            'openapi': OpenAPIRenderer,
            'openapi-json': JSONOpenAPIRenderer,
        }[format]

        return renderer_cls()
