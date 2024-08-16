import os

import braintree


def token():
    return gateway().client_token.generate()


def gateway():
    return braintree.BraintreeGateway(
        braintree.Configuration(
            environment=braintree.Environment.Sandbox,
            merchant_id=os.getenv("BRAINTREE_MERCHANT_ID"),
            public_key=os.getenv("BRAINTREE_PUBLIC_KEY"),
            private_key=os.getenv("BRAINTREE_PRIVATE_KEY"),
        )
    )
