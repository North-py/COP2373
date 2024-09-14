import re

# List of common spam keywords and phrases
spam_keywords = [
    "free", "winner", "cash", "prize", "guaranteed", "offer", "limited time", "act now",
    "click here", "buy direct", "exclusive deal", "money back", "save big", "special promotion",
    "unsecured credit", "credit card offer", "debt relief", "earn money", "free access",
    "free membership", "free quote", "free trial", "instant", "lowest price",
    "online biz opportunity", "risk-free", "win big", "make money", "million dollars",
    "unsecured loan"
]

def calculate_spam_score(email_message):
    spam_score = 0
    found_keywords = []
    
    # Convert the email message to lowercase for case-insensitive comparison
    email_message_lower = email_message.lower()
    
    # Check for each keyword in the email message
    for keyword in spam_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', email_message_lower):
            spam_score += 1
            found_keywords.append(keyword)
    
    return spam_score, found_keywords

def rate_spam_likelihood(spam_score):
    if spam_score >= 20:
        return "Very High"
    elif spam_score >= 10:
        return "High"
    elif spam_score >= 5:
        return "Moderate"
    else:
        return "Low"

def main():
    # Get the email message from the user
    email_message = input("Enter the email message: ")
    
    # Calculate the spam score and find keywords
    spam_score, found_keywords = calculate_spam_score(email_message)
    
    # Rate the likelihood of spam
    spam_likelihood = rate_spam_likelihood(spam_score)
    
    # Display results
    print(f"Spam Score: {spam_score}")
    print(f"Likelihood of Spam: {spam_likelihood}")
    if found_keywords:
        print("Keywords/Phrases causing the spam score:")
        for keyword in found_keywords:
            print(f"- {keyword}")

if __name__ == "__main__":
    main()
