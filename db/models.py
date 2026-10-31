# Base database configuration
# Bug introduced for testing: column renamed without updating client queries
user_id = Column(Integer, name="account_identifier")
