def get_by_slug(objs, slug):
    for obj in objs:
        if obj.slug == slug:
            return obj