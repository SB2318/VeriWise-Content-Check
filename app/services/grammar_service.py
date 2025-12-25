import language_tool_python
import html
from bs4 import BeautifulSoup
from functools import lru_cache
from app.utils.util import get_html_content

#Reuse the language tool
@lru_cache(maxsize=1)
def get_tool():
    return language_tool_python.LanguageTool('en-US')

class GrammarService:

    # FOR ADMIN APP
    @staticmethod
    def parse_text(text):
        # Use the BeautiSoup library to parse html text first
       
        soup = BeautifulSoup(text, 'html.parser')
        # get space separated plain text
        plainText = soup.get_text(separator = ' ')
        tool = get_tool()

        matches = tool.check(text)

        is_correct = len(matches) == 0

        # Calculate corrected percentage and find suggestions
        totalLength = len(plainText)
        errorLengthSum = sum([m.errorLength for m in matches])
        correction_percentage = 100.0 * (1 - (errorLengthSum / totalLength)) if totalLength else 100.0

        # predict approval
        approval = correction_percentage >= 90.0
        score_out_of_10 = round((correction_percentage / 100.0) * 10, 2)
        
        #predict suggestions
        #suggestions = []
        #for match in matches:
            #suggestions.append({
                #'suggested': match.replacements,
                #'start': match.offset,
                #'length': match.errorLength,
                #'ruleId': match.ruleId,
                #'message': match.message,
                #'context': match.context
#})
        
    
        # suggestions = [(m.ruleId, m.message, m.replacements, ) for m in matches]
        return {
            'corrected': is_correct,
            'correction_percentage': round(correction_percentage, 2),
            'approved': approval,
            'score': score_out_of_10
        }

   # FOR USER APP
    @staticmethod
    def render_grammar_suggestion(text):
         # First get html content
         ## Why? Cause, current setup of the method always expect an HTML content
        text = get_html_content(text)
        soup = BeautifulSoup(text, 'html.parser')
        paragraphs = soup.find_all(['p', 'h1', 'h2','h3'])
        tool = get_tool()

        edits = []
        for tag in paragraphs:
         #print(tag)
         original_text = tag.get_text()
         matches = tool.check(original_text)
      

         for match in sorted(matches, key=lambda m: m.offset, reverse=True):
            #print(f"Match: {match}, Replacements: {match.replacements}, Type: {type(match.replacements)}")

            if match.replacements and len(match.replacements) > 0:
              #print(match.replacements)
              start, end = match.offset, match.offset + match.errorLength
              replacement =  match.replacements[0]
              
              # Inject <span> tag with suggestion
              
              if start >= 0 and end <= len(original_text):
                 suggestion_html = (
                        f"<span style='background-color: yellow;' title='Suggested: {replacement}'>"
                        f"{replacement}</span>"
                    )

                 edits.append((start, end, suggestion_html))

         for start, end, suggestion_html in sorted(edits, key=lambda x: x[0], reverse=True):
            original_text = original_text[:start] + suggestion_html + original_text[end:]
           
         tag.clear()
         tag.append(BeautifulSoup(original_text, 'html.parser'))
        res = str(soup)

        return {
            'original': text,
            'suggestions': res
        }



     