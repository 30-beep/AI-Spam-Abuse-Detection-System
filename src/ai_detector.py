abusive_words = ["stupid", "idiot", "hate", "dumb"]
spam_words = ["buy now", "click here", "free money"]

def analyze_comment(comment):

    comment = comment.lower()

    for word in abusive_words:
        if word in comment:
            return "Abusive Content"

    for word in spam_words:
        if word in comment:
            return "Spam"
