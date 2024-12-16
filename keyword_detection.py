def keyword_detection(user_input):
    """
    Detect specific keywords in the user input.
    """
    user_input_lower = user_input.lower()

    if "hi" in user_input_lower:
        return "hi! How can I help you today?"

    if "hello" in user_input_lower:
        return "hello! wish you a good day!"

    # add more keywords here

    return None
