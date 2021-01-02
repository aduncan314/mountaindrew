import logging

import mistune
from django import template
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

logger = logging.getLogger('django')
register = template.Library()


class HighlightRenderer(mistune.Renderer):
    """
    Mistune renderer for formatting code in blog posts.

    Render Markdown including inline and block code snippets. Block code
    code snippets will pass the first token as `lang` to apply the appropriate
    formatting.

    Source: https://pypi.org/project/mistune/
    """

    def block_code(self, code, lang=None):
        try:
            lexer = get_lexer_by_name(lang, stripall=True)
            formatter = HtmlFormatter()
            return highlight(code, lexer, formatter)
        except Exception as e:
            logger.error(e)
            return '\n<pre><code>%s</code></pre>\n' % \
                   mistune.escape(code)


@register.filter
def markdown(value):
    """
    Markdown filter for formatting markdown and code formatting in blog posts.
    """
    renderer = HighlightRenderer()
    md = mistune.Markdown(renderer=renderer)
    return md(value)
