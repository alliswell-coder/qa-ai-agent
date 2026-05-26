Business Requirements Document
Amazon Checkout Flow

Document Info
FieldDetailProjectAmazon E-Commerce PlatformModuleOrder ManagementFeatureCheckout FlowVersion1.0DateMay 25, 2026Prepared ByQA Team

1. Purpose
Enable a logged-in user to successfully purchase one or more items from their cart through a secure, streamlined checkout process.

2. Scope
Covers the entire checkout journey — from Cart Review to Order Confirmation.

3. Checkout Flow Overview
Cart Review 
    ↓
Delivery Address
    ↓
Delivery Speed
    ↓
Payment Method
    ↓
Order Review
    ↓
Place Order
    ↓
Order Confirmation

4. Functional Requirements
4.1 Cart Review Page
RequirementDetailDisplay all itemsShow product name, image, quantity, priceQuantity updateUser can increase/decrease quantityRemove itemUser can remove item from cartPrice calculationSubtotal updates instantly on quantity changeEmpty cartShow "Your cart is empty" with Shop Now buttonProceed button"Proceed to Checkout" enabled only if cart has itemsSaved for laterUser can move item to Saved for Later list

4.2 Delivery Address Page
RequirementDetailDefault addressPre-populate with user's saved default addressAdd new addressUser can add a new delivery addressEdit addressUser can edit existing saved addressSelect addressUser can select from multiple saved addressesRequired fieldsName, Street, City, State, ZIP, Country, PhoneZIP validationZIP must match selected StateInternationalSupport US addresses only (in scope)

4.3 Delivery Speed Page
OptionDelivery TimeCostStandard Shipping5-7 business daysFree (orders $35+)Fast Shipping2-3 business days$5.99One-Day DeliveryNext business day$12.99Prime Free Same DaySame day (Prime only)Free
Rules:

Non-Prime users cannot see Prime options
If item is not eligible for One-Day → grey it out
Default selection = Standard Shipping


4.4 Payment Method Page
Payment TypeSupportedSaved Credit/Debit CardYesAdd New CardYesAmazon Gift CardYesAmazon Pay LaterYesPayPalNo (out of scope)
Rules:
ConditionBehaviorExpired cardShow "Card expired" — do not allow selectionInsufficient gift card balanceApply partial balance → charge remaining to cardInvalid new card numberShow inline errorCVV missingBlock submission, show errorBilling address differentAllow user to enter separate billing address

4.5 Order Review Page
RequirementDetailShow full summaryItems, address, delivery speed, paymentShow price breakdownSubtotal + Shipping + Tax = TotalPromo code fieldUser can apply/remove promo codeInvalid promoShow "Invalid or expired promo code"Valid promoShow discount applied to totalEdit optionUser can go back and edit any sectionPlace Order buttonClearly visible, single click only

4.6 Place Order
ConditionBehaviorSuccessful paymentRedirect to Order Confirmation pagePayment declinedShow "Payment failed" — stay on review pageItem goes out of stock at checkoutShow "Item no longer available" errorDouble click on Place OrderProcess only ONE order — no duplicatesSession timeout during checkoutRedirect to login — cart preserved

4.7 Order Confirmation Page
RequirementDetailOrder numberDisplay unique order IDSummaryShow items ordered, delivery date, addressConfirmation emailSent within 2 minutes to registered emailContinue ShoppingButton redirects to Amazon homepageTrack Order linkVisible immediately after order placed

5. Non-Functional Requirements
TypeRequirementPerformanceEach checkout page loads under 3 secondsSecurityPayment data encrypted via TLS 1.2+SessionCheckout session expires after 30 mins idleAvailability99.9% uptime during checkout flowMobileFully responsive on iOS and Android browsers

6. Out of Scope

Guest checkout
Subscribe & Save orders
Business Prime accounts
International shipping
Returns and refunds


