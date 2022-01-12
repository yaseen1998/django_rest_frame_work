from rest_framework.throttling import UserRateThrottle

class ReviewCreateTh(UserRateThrottle):
    scope = 'review-create'
class ReviewListTh(UserRateThrottle):
    scope = 'review-list'