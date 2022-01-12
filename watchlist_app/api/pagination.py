from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 4
    # page_query_param = 'p'
    # page_size_query_param = 'size'
    # max_page_size =10
    # last_page_strings = 'end' 
    
class WatchListLimit(LimitOffsetPagination):
    default_limit = 5
    max_limit = 5
    limit_query_param = 'start'
    offset_query_param = 'from'
    
class WatchListCursor(CursorPagination):
    page_size=5
    # ordering = 'created'
    cursor_query_param  = 'record'