def get_intent_and_answer(text):
    # Simulate simple intent detection
    if "password" in text.lower():
        return "Password Reset", "Please click on 'Forgot Password' on the login screen."
    elif "billing" in text.lower():
        return "Billing Info", "You can update billing info in your account settings."
    else:
        return "General Query", "Please contact customer support."
