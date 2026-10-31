# Base payment service setup
print("Initializing service")

# Bug introduced for testing
stripe_token = os.environ["STRIPE_API_SECRET"]
stripe.initialize(token=stripe_token)
