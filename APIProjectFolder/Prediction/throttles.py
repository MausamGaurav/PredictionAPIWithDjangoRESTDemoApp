from rest_framework.throttling import UserRateThrottle

# Custom Throttle classes
class LimitedRateThrottle(UserRateThrottle):
    scope = 'limited' 

class BurstRateThrottle(UserRateThrottle):
    scope = 'burst'