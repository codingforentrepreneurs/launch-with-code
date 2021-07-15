from joins.models import Join


class ReferMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        ref_id = request.GET.get("ref")
        if ref_id is not None:
            try:
                obj = Join.objects.get(ref_id = ref_id)
            except:
                obj = None
            if obj:
                request.session['join_id_ref'] = obj.id
        # Code to be executed for each request/response after
        # the view is called.
        return response