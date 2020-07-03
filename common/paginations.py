from rest_framework.pagination import PageNumberPagination


class StandardPagePagination(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 1000
    page_size = 30

    def get_paginated_response(self, data, *args, **kwargs):
        response = super().get_paginated_response(data, *args, **kwargs)
        response.data['page'] = self.page.number
        response.data['page_size'] = self.get_page_size(self.request)
        # del response.data['next']
        # del response.data['previous']
        response.data.move_to_end('results')
        return response
