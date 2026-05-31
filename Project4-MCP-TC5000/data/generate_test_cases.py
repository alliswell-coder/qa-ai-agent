import json
import csv
import random

# Module configurations for 500 test cases
MODULES = [
    {"name": "Login", "count": 50},
    {"name": "Cart", "count": 50},
    {"name": "Address", "count": 50},
    {"name": "Delivery", "count": 50},
    {"name": "Payment", "count": 50},
    {"name": "Order Review", "count": 50},
    {"name": "Order Confirmation", "count": 50},
    {"name": "Edge Cases", "count": 50},
    {"name": "Negative Cases", "count": 50},
    {"name": "Performance", "count": 50}
]

# Test case templates for each module (NEW FORMAT with "should" language)
TEST_TEMPLATES = {
    "Login": [
        {
            "description": "Verify if the user is able to login successfully with valid credentials",
            "steps": [
                {"action": "Open the portal", "expected": "Portal should be opened successfully"},
                {"action": "Enter valid email address", "expected": "Email should be accepted"},
                {"action": "Enter valid password", "expected": "Password should be accepted"},
                {"action": "Click on login button", "expected": "User should be logged in successfully"},
                {"action": "Verify dashboard", "expected": "Dashboard should be displayed"}
            ]
        },
        {
            "description": "Verify if the user is unable to login with invalid email",
            "steps": [
                {"action": "Open the portal", "expected": "Portal should be opened successfully"},
                {"action": "Enter invalid email address", "expected": "Email should be rejected"},
                {"action": "Enter valid password", "expected": "Password should be accepted"},
                {"action": "Click on login button", "expected": "Error message should be displayed"}
            ]
        },
        {
            "description": "Verify if the user is unable to login with invalid password",
            "steps": [
                {"action": "Open the portal", "expected": "Portal should be opened successfully"},
                {"action": "Enter valid email address", "expected": "Email should be accepted"},
                {"action": "Enter invalid password", "expected": "Password should be rejected"},
                {"action": "Click on login button", "expected": "Error message should be displayed"}
            ]
        },
        {
            "description": "Verify if the user is unable to login with empty credentials",
            "steps": [
                {"action": "Open the portal", "expected": "Portal should be opened successfully"},
                {"action": "Leave email field empty", "expected": "Field should remain empty"},
                {"action": "Leave password field empty", "expected": "Field should remain empty"},
                {"action": "Click on login button", "expected": "Validation error should be displayed"}
            ]
        },
        {
            "description": "Verify if the user is able to login using social media account",
            "steps": [
                {"action": "Open the portal", "expected": "Portal should be opened successfully"},
                {"action": "Click on social media login button", "expected": "Social media auth popup should open"},
                {"action": "Authorize social media account", "expected": "Authorization should be successful"},
                {"action": "Complete login process", "expected": "User should be logged in successfully"}
            ]
        }
    ],
    "Cart": [
        {
            "description": "Verify if the user is able to add a single item to cart",
            "steps": [
                {"action": "Navigate to product page", "expected": "Product page should load successfully"},
                {"action": "Select quantity", "expected": "Quantity should be selected"},
                {"action": "Click on Add to Cart button", "expected": "Item should be added to cart"},
                {"action": "View cart", "expected": "Cart should display the item"},
                {"action": "Verify item details", "expected": "Item details should be correct"}
            ]
        },
        {
            "description": "Verify if the user is able to add multiple items to cart",
            "steps": [
                {"action": "Navigate to first product", "expected": "Product page should load successfully"},
                {"action": "Add to cart", "expected": "Item should be added"},
                {"action": "Navigate to second product", "expected": "Product page should load successfully"},
                {"action": "Add to cart", "expected": "Item should be added"},
                {"action": "View cart", "expected": "Cart should show both items"}
            ]
        },
        {
            "description": "Verify if the user is able to remove item from cart",
            "steps": [
                {"action": "Open cart", "expected": "Cart should display"},
                {"action": "Click on remove button", "expected": "Remove confirmation should appear"},
                {"action": "Confirm removal", "expected": "Item should be removed from cart"},
                {"action": "Verify cart is empty", "expected": "Cart should be empty"}
            ]
        },
        {
            "description": "Verify if the user is able to update item quantity",
            "steps": [
                {"action": "Open cart", "expected": "Cart should display"},
                {"action": "Change quantity", "expected": "Quantity should be updated"},
                {"action": "Verify price update", "expected": "Total price should be updated"}
            ]
        },
        {
            "description": "Verify if the user is able to save item for later",
            "steps": [
                {"action": "Open cart", "expected": "Cart should display"},
                {"action": "Click on Save for Later", "expected": "Item should be moved to saved list"},
                {"action": "Verify saved list", "expected": "Item should appear in saved list"}
            ]
        }
    ],
    "Address": [
        {
            "description": "Verify if the user is able to add new delivery address",
            "steps": [
                {"action": "Navigate to address settings", "expected": "Address page should load successfully"},
                {"action": "Click on Add Address button", "expected": "Address form should appear"},
                {"action": "Fill address details", "expected": "Details should be entered"},
                {"action": "Click on Save button", "expected": "Address should be saved successfully"}
            ]
        },
        {
            "description": "Verify if the user is able to edit existing address",
            "steps": [
                {"action": "Navigate to address settings", "expected": "Address page should load successfully"},
                {"action": "Click on Edit on address", "expected": "Edit form should appear"},
                {"action": "Modify address details", "expected": "Details should be modified"},
                {"action": "Click on Save button", "expected": "Address should be updated successfully"}
            ]
        },
        {
            "description": "Verify if the user is able to delete address",
            "steps": [
                {"action": "Navigate to address settings", "expected": "Address page should load successfully"},
                {"action": "Click on Delete on address", "expected": "Delete confirmation should appear"},
                {"action": "Confirm deletion", "expected": "Address should be deleted successfully"}
            ]
        },
        {
            "description": "Verify if the user is able to set default address",
            "steps": [
                {"action": "Navigate to address settings", "expected": "Address page should load successfully"},
                {"action": "Click on Set Default", "expected": "Address should be marked as default"},
                {"action": "Verify default status", "expected": "Default badge should be displayed"}
            ]
        },
        {
            "description": "Verify if the user is unable to add address with invalid ZIP",
            "steps": [
                {"action": "Navigate to address settings", "expected": "Address page should load successfully"},
                {"action": "Click on Add Address button", "expected": "Address form should appear"},
                {"action": "Enter invalid ZIP code", "expected": "ZIP should be entered"},
                {"action": "Click on Save button", "expected": "Validation error should be displayed"}
            ]
        }
    ],
    "Delivery": [
        {
            "description": "Verify if the user is able to select standard delivery",
            "steps": [
                {"action": "Proceed to checkout", "expected": "Checkout page should load successfully"},
                {"action": "Navigate to delivery options", "expected": "Delivery options should be displayed"},
                {"action": "Select standard delivery", "expected": "Option should be selected"},
                {"action": "Click on Continue", "expected": "Delivery option should be confirmed"}
            ]
        },
        {
            "description": "Verify if the user is able to select express delivery",
            "steps": [
                {"action": "Proceed to checkout", "expected": "Checkout page should load successfully"},
                {"action": "Navigate to delivery options", "expected": "Delivery options should be displayed"},
                {"action": "Select express delivery", "expected": "Option should be selected"},
                {"action": "Click on Continue", "expected": "Delivery option should be confirmed"}
            ]
        },
        {
            "description": "Verify if the user is able to select same-day delivery",
            "steps": [
                {"action": "Proceed to checkout", "expected": "Checkout page should load successfully"},
                {"action": "Navigate to delivery options", "expected": "Delivery options should be displayed"},
                {"action": "Select same-day delivery", "expected": "Option should be selected"},
                {"action": "Click on Continue", "expected": "Delivery option should be confirmed"}
            ]
        },
        {
            "description": "Verify if the user is able to view delivery date estimate",
            "steps": [
                {"action": "Select delivery option", "expected": "Option should be selected"},
                {"action": "View delivery date", "expected": "Date estimate should be displayed"},
                {"action": "Verify date accuracy", "expected": "Date should be reasonable"}
            ]
        },
        {
            "description": "Verify if the user is able to select delivery time slot",
            "steps": [
                {"action": "Select same-day delivery", "expected": "Time slots should be displayed"},
                {"action": "Choose time slot", "expected": "Time slot should be selected"},
                {"action": "Click on Continue", "expected": "Time slot should be confirmed"}
            ]
        }
    ],
    "Payment": [
        {
            "description": "Verify if the user is able to pay with saved credit card",
            "steps": [
                {"action": "Navigate to payment", "expected": "Payment page should load successfully"},
                {"action": "Select saved card", "expected": "Card should be selected"},
                {"action": "Enter CVV", "expected": "CVV should be accepted"},
                {"action": "Click on Place Order", "expected": "Payment should be processed successfully"}
            ]
        },
        {
            "description": "Verify if the user is able to add new credit card",
            "steps": [
                {"action": "Navigate to payment", "expected": "Payment page should load successfully"},
                {"action": "Click on Add new card", "expected": "Card form should appear"},
                {"action": "Enter card details", "expected": "Details should be entered"},
                {"action": "Click on Save card", "expected": "Card should be saved successfully"}
            ]
        },
        {
            "description": "Verify if the user is able to pay with gift card",
            "steps": [
                {"action": "Navigate to payment", "expected": "Payment page should load successfully"},
                {"action": "Select gift card option", "expected": "Gift card should be selected"},
                {"action": "Enter gift card code", "expected": "Code should be validated"},
                {"action": "Apply payment", "expected": "Payment should be processed"}
            ]
        },
        {
            "description": "Verify if the user is able to pay with Amazon Pay",
            "steps": [
                {"action": "Navigate to payment", "expected": "Payment page should load successfully"},
                {"action": "Select Amazon Pay", "expected": "Amazon Pay should be selected"},
                {"action": "Authorize payment", "expected": "Authorization should be successful"},
                {"action": "Complete order", "expected": "Order should be placed successfully"}
            ]
        },
        {
            "description": "Verify if payment is declined with invalid card",
            "steps": [
                {"action": "Navigate to payment", "expected": "Payment page should load successfully"},
                {"action": "Select invalid card", "expected": "Card should be selected"},
                {"action": "Click on Place Order", "expected": "Payment declined error should be displayed"}
            ]
        }
    ],
    "Order Review": [
        {
            "description": "Verify if the user is able to review order summary",
            "steps": [
                {"action": "Navigate to order review", "expected": "Review page should load successfully"},
                {"action": "Verify item details", "expected": "Details should be correct"},
                {"action": "Verify shipping address", "expected": "Address should be correct"},
                {"action": "Verify payment method", "expected": "Payment should be correct"}
            ]
        },
        {
            "description": "Verify if the user is able to apply promo code",
            "steps": [
                {"action": "Navigate to order review", "expected": "Review page should load successfully"},
                {"action": "Enter promo code", "expected": "Code should be entered"},
                {"action": "Apply code", "expected": "Discount should be applied"},
                {"action": "Verify discount", "expected": "Total should be updated"}
            ]
        },
        {
            "description": "Verify if the user is able to remove promo code",
            "steps": [
                {"action": "Navigate to order review", "expected": "Review page should load successfully"},
                {"action": "Click on remove promo", "expected": "Promo should be removed"},
                {"action": "Verify total", "expected": "Total should be updated"}
            ]
        },
        {
            "description": "Verify if the user is able to add gift message",
            "steps": [
                {"action": "Navigate to order review", "expected": "Review page should load successfully"},
                {"action": "Click on add gift message", "expected": "Message field should appear"},
                {"action": "Enter message", "expected": "Message should be entered"},
                {"action": "Save message", "expected": "Message should be saved"}
            ]
        },
        {
            "description": "Verify if the user is able to select gift wrap",
            "steps": [
                {"action": "Navigate to order review", "expected": "Review page should load successfully"},
                {"action": "Select gift wrap option", "expected": "Option should be selected"},
                {"action": "Verify charge", "expected": "Charge should be added to total"}
            ]
        }
    ],
    "Order Confirmation": [
        {
            "description": "Verify if the user is able to place order successfully",
            "steps": [
                {"action": "Click on Place Order", "expected": "Order processing should start"},
                {"action": "Wait for confirmation", "expected": "Confirmation page should load"},
                {"action": "Verify order ID", "expected": "Order ID should be displayed"},
                {"action": "Save order details", "expected": "Details should be saved"}
            ]
        },
        {
            "description": "Verify if the user receives order confirmation email",
            "steps": [
                {"action": "Place order", "expected": "Order should be placed successfully"},
                {"action": "Check email", "expected": "Email should be received"},
                {"action": "Verify email content", "expected": "Content should be correct"}
            ]
        },
        {
            "description": "Verify if the user is able to view order in order history",
            "steps": [
                {"action": "Navigate to orders", "expected": "Orders page should load successfully"},
                {"action": "Find recent order", "expected": "Order should be displayed"},
                {"action": "Click on order details", "expected": "Details should be displayed"}
            ]
        },
        {
            "description": "Verify if the user is able to cancel order immediately",
            "steps": [
                {"action": "Navigate to orders", "expected": "Orders page should load successfully"},
                {"action": "Select recent order", "expected": "Order should be selected"},
                {"action": "Click on cancel", "expected": "Cancellation should be processed"}
            ]
        },
        {
            "description": "Verify if the user is able to track order status",
            "steps": [
                {"action": "Navigate to orders", "expected": "Orders page should load successfully"},
                {"action": "Select order", "expected": "Order should be selected"},
                {"action": "View tracking", "expected": "Tracking info should be displayed"}
            ]
        }
    ],
    "Edge Cases": [
        {
            "description": "Verify if the user is able to login with special characters in email",
            "steps": [
                {"action": "Navigate to login", "expected": "Login page should load successfully"},
                {"action": "Enter email with special characters", "expected": "Email should be accepted"},
                {"action": "Enter password", "expected": "Password should be accepted"},
                {"action": "Click on login", "expected": "Login should be successful"}
            ]
        },
        {
            "description": "Verify if the user is able to add maximum quantity to cart",
            "steps": [
                {"action": "Enter maximum quantity", "expected": "Quantity should be set"},
                {"action": "Add to cart", "expected": "Item should be added"},
                {"action": "Verify cart", "expected": "Maximum quantity should be shown"}
            ]
        },
        {
            "description": "Verify if the user is able to enter international address format",
            "steps": [
                {"action": "Navigate to address", "expected": "Address page should load successfully"},
                {"action": "Enter international address", "expected": "Address should be entered"},
                {"action": "Save address", "expected": "Address should be saved"}
            ]
        },
        {
            "description": "Verify if the user is able to apply multiple promo codes",
            "steps": [
                {"action": "Apply first promo code", "expected": "First discount should be applied"},
                {"action": "Apply second promo code", "expected": "Second discount should be applied"},
                {"action": "Verify total", "expected": "Both discounts should be reflected"}
            ]
        },
        {
            "description": "Verify if the system handles very long gift message",
            "steps": [
                {"action": "Enter very long message", "expected": "Message should be entered"},
                {"action": "Save message", "expected": "Message should be saved or truncated"}
            ]
        }
    ],
    "Negative Cases": [
        {
            "description": "Verify if the user is unable to login with expired session",
            "steps": [
                {"action": "Navigate to amazon.com", "expected": "Homepage should load successfully"},
                {"action": "Try to access account", "expected": "User should be redirected to login"}
            ]
        },
        {
            "description": "Verify if the user is unable to add out of stock item",
            "steps": [
                {"action": "Navigate to product", "expected": "Product page should load successfully"},
                {"action": "Click on Add to Cart", "expected": "Out of stock message should be displayed"}
            ]
        },
        {
            "description": "Verify if payment is declined with invalid payment method",
            "steps": [
                {"action": "Enter invalid card", "expected": "Card should be entered"},
                {"action": "Place order", "expected": "Payment should be declined"}
            ]
        },
        {
            "description": "Verify if the system rejects expired promo code",
            "steps": [
                {"action": "Enter expired code", "expected": "Code should be entered"},
                {"action": "Apply code", "expected": "Expired code error should be displayed"}
            ]
        },
        {
            "description": "Verify if the user is unable to cancel shipped order",
            "steps": [
                {"action": "Navigate to orders", "expected": "Orders page should load successfully"},
                {"action": "Select shipped order", "expected": "Order should be selected"},
                {"action": "Click on cancel", "expected": "Cannot cancel error should be displayed"}
            ]
        }
    ],
    "Performance": [
        {
            "description": "Verify if the homepage loads within acceptable time",
            "steps": [
                {"action": "Navigate to amazon.com", "expected": "Page should load within 3 seconds"}
            ]
        },
        {
            "description": "Verify if the product page loads within acceptable time",
            "steps": [
                {"action": "Navigate to product", "expected": "Page should load within 3 seconds"}
            ]
        },
        {
            "description": "Verify if adding to cart completes within acceptable time",
            "steps": [
                {"action": "Click on Add to Cart", "expected": "Item should be added within 2 seconds"}
            ]
        },
        {
            "description": "Verify if search response is within acceptable time",
            "steps": [
                {"action": "Enter search query", "expected": "Results should load within 2 seconds"}
            ]
        },
        {
            "description": "Verify if checkout process completes within acceptable time",
            "steps": [
                {"action": "Complete checkout flow", "expected": "Process should complete within 30 seconds"}
            ]
        }
    ]
}

def generate_test_case(tc_id, module, template):
    """Generate a single test case based on template (NEW FORMAT)"""
    test_case = {
        "TC_ID": tc_id,
        "Scenario": module,
        "Description": template["description"],
        "steps": template["steps"].copy()
    }
    return test_case

def generate_all_test_cases():
    """Generate all 500 test cases (NEW FORMAT)"""
    test_cases = []
    tc_counter = 1
    
    for module_config in MODULES:
        module_name = module_config["name"]
        count = module_config["count"]
        
        templates = TEST_TEMPLATES[module_name]
        
        for i in range(count):
            tc_id = f"TC{tc_counter:03d}"
            # Cycle through templates
            template = templates[i % len(templates)]
            
            # Add variation to description for uniqueness
            variation = (i // len(templates)) + 1
            if variation > 1:
                modified_template = template.copy()
                modified_template["steps"] = [step.copy() for step in template["steps"]]
                modified_template["description"] = f"{template['description']} - Variant {variation}"
                test_case = generate_test_case(tc_id, module_name, modified_template)
            else:
                test_case = generate_test_case(tc_id, module_name, template)
            
            test_cases.append(test_case)
            tc_counter += 1
    
    return test_cases

def main():
    """Main function to generate and save test cases (NEW FORMAT)"""
    print("Generating 500 test cases...")
    test_cases = generate_all_test_cases()
    
    print(f"Generated {len(test_cases)} test cases")
    
    # Save to JSON file
    json_file = "test_cases.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(test_cases, f, indent=2)
    
    print(f"Test cases saved to {json_file}")
    
    # Print summary
    module_counts = {}
    for tc in test_cases:
        module = tc["Scenario"]
        module_counts[module] = module_counts.get(module, 0) + 1
    
    print("\nSummary by module:")
    for module, count in module_counts.items():
        print(f"  {module}: {count} test cases")

if __name__ == "__main__":
    main()
