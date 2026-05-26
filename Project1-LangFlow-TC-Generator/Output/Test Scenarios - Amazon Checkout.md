# Agent 1 — Sample Output: Amazon Checkout Flow Test Cases

## Cart Review Page (TC001-TC015)

| TC ID | Description | Pre-condition | Steps | Expected Result | Priority | Type |
|-------|-------------|---------------|-------|-----------------|----------|------|
| TC001 | Login | Valid account exists | User logs in | User is logged in | High | Positive |
| TC002 | Add to Cart | TC001 - user is logged in | User adds item to cart | Item is added to cart | High | Positive |
| TC003 | Proceed to Checkout | TC002 - item in cart | User clicks "Proceed to Checkout" | Cart Review page loads | High | Positive |
| TC004 | Empty Cart | TC002 - item in cart | User removes all items from cart | "Your cart is empty" message appears | High | Positive |
| TC005 | Remove Item | TC002 - item in cart | User removes item from cart | Item is removed from cart | High | Positive |
| TC006 | Update Quantity | TC002 - item in cart | User updates quantity of item | Quantity is updated | High | Positive |
| TC007 | Invalid Quantity | TC002 - item in cart | User enters invalid quantity | Error message appears | High | Negative |
| TC008 | Saved for Later | TC002 - item in cart | User moves item to Saved for Later list | Item is moved to Saved for Later list | High | Positive |
| TC009 | Proceed to Checkout with Saved for Later | TC008 - item in Saved for Later list | User clicks "Proceed to Checkout" | Cart Review page loads | High | Positive |
| TC010 | Cart Review with Multiple Items | TC002 - multiple items in cart | User views cart with multiple items | Multiple items are displayed | High | Positive |
| TC011 | Cart Review with No Items | TC004 - cart is empty | User views cart with no items | "Your cart is empty" message appears | High | Positive |
| TC012 | Cart Review with Single Item | TC002 - single item in cart | User views cart with single item | Single item is displayed | High | Positive |
| TC013 | Empty Saved for Later List | TC008 - list is empty | User views empty Saved for Later list | "Your Saved for Later list is empty" appears | High | Positive |
| TC014 | Multiple Saved for Later Items | TC008 - multiple items in list | User views multiple Saved for Later items | Multiple items are displayed | High | Positive |
| TC015 | Saved for Later + Multiple Cart Items | TC008 - item in list and multiple in cart | User views cart with both | Both are displayed correctly | High | Positive |

---

## Delivery Address Page (TC016-TC030)

| TC ID | Description | Pre-condition | Steps | Expected Result | Priority | Type |
|-------|-------------|---------------|-------|-----------------|----------|------|
| TC016 | Default Address | TC001 - user logged in | User views delivery address page | Default address is displayed | High | Positive |
| TC017 | Add New Address | TC001 - user logged in | User adds new address | New address is added | High | Positive |
| TC018 | Edit Address | TC001 - user logged in | User edits existing address | Address is updated | High | Positive |
| TC019 | Select Address | TC001 - user logged in | User selects from saved addresses | Selected address is displayed | High | Positive |
| TC020 | Required Fields Missing | TC001 - user logged in | User saves address with missing fields | Error message appears | High | Negative |
| TC021 | Invalid ZIP Code | TC001 - user logged in | User enters invalid ZIP | Error message appears | High | Negative |
| TC022 | International Address | TC001 - user logged in | User adds international address | Error message appears | High | Negative |
| TC023 | Default + Multiple Saved Addresses | TC001 - multiple saved addresses | User views address page | Default and all saved addresses displayed | High | Positive |
| TC024 | Add Address with Multiple Saved | TC001 - multiple saved addresses | User adds new address | New address added alongside existing | High | Positive |
| TC025 | Edit Address with Multiple Saved | TC001 - multiple saved addresses | User edits an address | Address updated, others unchanged | High | Positive |
| TC026 | Select from Multiple Saved | TC001 - multiple saved addresses | User selects an address | Selected address highlighted | High | Positive |
| TC027 | Missing Fields + Multiple Saved | TC001 - multiple saved addresses | User saves with missing fields | Error message appears | High | Negative |
| TC028 | Invalid ZIP + Multiple Saved | TC001 - multiple saved addresses | User enters invalid ZIP | Error message appears | High | Negative |
| TC029 | International + Multiple Saved | TC001 - multiple saved addresses | User adds international address | Error message appears | High | Negative |
| TC030 | Default Address + Saved for Later | TC008 - item in Saved for Later | User views address page | Default address and Saved for Later shown | High | Positive |

---

## Delivery Speed Page (TC031-TC045)

| TC ID | Description | Pre-condition | Steps | Expected Result | Priority | Type |
|-------|-------------|---------------|-------|-----------------|----------|------|
| TC031 | Standard Shipping | TC001 - user logged in | User views delivery speed page | Standard shipping option displayed | High | Positive |
| TC032 | Fast Shipping | TC001 - user logged in | User views delivery speed page | Fast shipping option displayed | High | Positive |
| TC033 | One-Day Delivery | TC001 - user logged in | User views delivery speed page | One-day delivery option displayed | High | Positive |
| TC034 | Prime Free Same Day | TC001 - Prime user logged in | User views delivery speed page | Prime same day option displayed | High | Positive |
| TC035 | Non-Prime User Options | TC001 - non-Prime user | User views delivery speed page | Prime options not shown | High | Negative |
| TC036 | Item Not Eligible for One-Day | TC001 - ineligible item in cart | User views delivery speed page | One-day delivery greyed out | High | Edge Case |
| TC037 | Default Selection | TC001 - user logged in | User views delivery speed page | Standard shipping selected by default | High | Positive |
| TC038 | Select Standard Shipping | TC001 - user logged in | User selects standard shipping | Standard shipping selected | High | Positive |
| TC039 | Select Fast Shipping | TC001 - user logged in | User selects fast shipping | Fast shipping selected | High | Positive |
| TC040 | Select One-Day Delivery | TC001 - user logged in | User selects one-day delivery | One-day delivery selected | High | Positive |
| TC041 | Select Prime Same Day | TC001 - Prime user logged in | User selects Prime same day | Prime same day selected | High | Positive |
| TC042 | Select Non-Prime Option | TC001 - non-Prime user | User selects non-Prime option | Non-Prime option selected | High | Positive |
| TC043 | Select Ineligible One-Day Item | TC001 - ineligible item in cart | User tries to select one-day | Error message appears | High | Negative |
| TC044 | Reselect Default Option | TC001 - user logged in | User reselects default | Default selection confirmed | High | Edge Case |
| TC045 | Standard Shipping + Saved for Later | TC008 - item in Saved for Later | User views delivery speed page | Standard shipping and Saved for Later shown | High | Positive |

---

## Payment Method Page (TC046-TC060)

| TC ID | Description | Pre-condition | Steps | Expected Result | Priority | Type |
|-------|-------------|---------------|-------|-----------------|----------|------|
| TC046 | Saved Credit/Debit Card | TC001 - user logged in | User views payment page | Saved card displayed | High | Positive |
| TC047 | Add New Card | TC001 - user logged in | User adds new card | New card added | High | Positive |
| TC048 | Amazon Gift Card | TC001 - user logged in | User views payment page | Gift card option displayed | High | Positive |
| TC049 | Amazon Pay Later | TC001 - user logged in | User views payment page | Pay Later option displayed | High | Positive |
| TC050 | Expired Card | TC001 - expired card saved | User selects expired card | "Card expired" error shown | High | Negative |
