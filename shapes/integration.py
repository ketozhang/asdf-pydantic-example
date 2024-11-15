import asdf
from asdf import AsdfFile
from astropy import units as u
from shapes.circle import Circle

import asdf
import yaml
from asdf.extension import Extension, TagDefinition
from asdf_pydantic import AsdfPydanticConverter

AsdfPydanticConverter.add_models(Circle)


class ShapesExtension(Extension):
    extension_uri = "asdf://asdf-pydantic/examples/extensions/shapes-1.0.0"
    converters = [AsdfPydanticConverter()]
    tags = [
        TagDefinition(Circle._tag, schema_uris=[Circle._tag + "/schema"]),
    ]


def get_extensions():
    return [ShapesExtension()]


def get_resource_mappings():
    schema = yaml.safe_load(Circle.model_asdf_schema())
    schema_str = yaml.dump(schema)

    logging.debug("\n%s", schema_str)

    return [{schema["id"]: schema_str}]
