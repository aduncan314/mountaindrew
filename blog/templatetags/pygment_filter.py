import mistune
import logging
from django import template
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

logger = logging.getLogger('django')
register = template.Library()


class HighlightRenderer(mistune.Renderer):
    """
    Mistune renderer use by Markdown class. Taken from mistune site example with better error handling
    """
    def block_code(self, code, lang=None):
        try:
            lexer = get_lexer_by_name(lang, stripall=True)
            formatter = HtmlFormatter()
            return highlight(code, lexer, formatter)
        except Exception as e:
            # Log error but don't worry
            logger.error(e)
            return '\n<pre><code>%s</code></pre>\n' % \
                   mistune.escape(code)


@register.filter
def markdown(value):
    renderer = HighlightRenderer()
    md = mistune.Markdown(renderer=renderer)
    return md(value)
