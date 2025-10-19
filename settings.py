INSTALLED_APPS = [
    ...,
    'graphene_django',
    'crm',
]

GRAPHENE = {
    'SCHEMA': 'crm.schema.schema'  # Update this line to point to your schema
}
