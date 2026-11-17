# Tags

Reusable named tags and many-to-many object associations. Each consuming module
defines its own tag and association tables by subclassing `GDO_Tag` and
`GDO_TagObject`, and exposes them through `WithTags` on its tagged object.

# Tags (For Humans)

Tags can be reused across objects of the same kind. Adding a tag that already
exists reuses it; assigning an already assigned tag is idempotent. Removing an
association does not delete the shared tag. New names require explicit opt-in.

## Methods

The storage API is for consuming modules; no public administration interface
is provided by itself.

## GDTs

`GDT_Tags` accepts comma-separated names. `.allow_creation()` opts into
creating unknown names; creation is off by default.

`GDT_TagCloud` renders reusable weighted links from `(id, name, count)` rows;
the caller supplies link generation and the selected tag.

## GDOs

`GDO_Tag` stores a name and `GDO_TagObject` associates a tag with an object.

# Tags (For ALs)

## Methods

Use `WithTags.get_tags()`, `add_tag(name, allow_creation=False)`, and
`remove_tag(name)` on persisted objects. Callers must authorize creation.

## GDTs

Configure `GDT_Tags(...).table(MyTag.table())`; call `resolve_tags()` only
after validation and authorization, then explicitly assign tags to an object.

## GDOs

Register concrete tag and association tables with the consuming module, along
with a `tags` dependency. Composite association keys prevent duplicate links.
