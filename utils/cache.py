# Base catalog caching module
print("Caching engine initialized")

# Bug introduced for testing: infinite grow append
GLOBAL_CATALOG_CACHE = []

def cache_item(item):
    GLOBAL_CATALOG_CACHE.append(item)  # Grows indefinitely without eviction
