from html import escape

def get_html_content(text: str) -> str:
        """
        Converts plain text into safe HTML content by escaping special characters
        and wrapping it in a <p> tag.

        :param text: Plain text to be converted.
        :return: HTML-safe string.
        """
        safe_text = escape(text)
        
        return f"""
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Grammar Suggestion</title>
</head>
<body>
    <h1>Grammar Suggestion</h1>
    <p>{text}</p>
</body>
</html>"""
