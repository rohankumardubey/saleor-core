from ...utils import get_graphql_content

CHECKOUT_BILLING_ADDRESS_UPDATE_MUTATION = """
mutation CheckoutBillingAddressUpdate(
  $billingAddress: AddressInput!, $checkoutId: ID!
) {
  checkoutBillingAddressUpdate(billingAddress: $billingAddress, id: $checkoutId) {
    errors {
      field
      code
      message
    }
    checkout {
      billingAddress {
        firstName
        lastName
        companyName
        streetAddress1
        postalCode
        country {
          code
        }
        city
        countryArea
        phone
      }
    }
  }
}
"""

DEFAULT_ADDRESS = {
    "firstName": "John Saleor",
    "lastName": "Doe Mirumee",
    "companyName": "Saleor Commerce",
    "streetAddress1": "14208 Hawthorne Blvd",
    "streetAddress2": "",
    "postalCode": "90250",
    "country": "US",
    "city": "Hawthorne",
    "countryArea": "CA",
    "phone": "+12025550163",
}


def checkout_billing_address_update(api_client, checkout_id, address=DEFAULT_ADDRESS):
    variables = {
        "checkoutId": checkout_id,
        "billingAddress": address,
    }
    response = api_client.post_graphql(
        CHECKOUT_BILLING_ADDRESS_UPDATE_MUTATION,
        variables=variables,
    )
    content = get_graphql_content(response)

    assert content["data"]["checkoutBillingAddressUpdate"]["errors"] == []

    data = content["data"]["checkoutBillingAddressUpdate"]["checkout"]
    assert data["billingAddress"]["firstName"] == address["firstName"]
    assert data["billingAddress"]["lastName"] == address["lastName"]
    assert data["billingAddress"]["companyName"] == address["companyName"]
    assert data["billingAddress"]["streetAddress1"] == address["streetAddress1"]
    assert data["billingAddress"]["postalCode"] == address["postalCode"]
    assert data["billingAddress"]["country"]["code"] == address["country"]
    assert data["billingAddress"]["city"] == address["city"].upper()
    assert data["billingAddress"]["countryArea"] == address["countryArea"]
    assert data["billingAddress"]["phone"] == address["phone"]

    return data