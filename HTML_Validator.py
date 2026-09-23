#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    tags = _extract_tags(html)
    stack = []
    for tag in tags:
        if tag[:2] == ('</'):
            tag_name = tag[2:-1]
            if not stack or stack[-1] != tag_name:
                return False
            stack.pop()
        else:
            tag_name = tag[1:-1]
            stack.append(tag_name)
    return len(stack) == 0


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = []
    current_tag = ""
    inside_tag = False
    for char in html:
        if char == "<":
            inside_tag = True
            current_tag = "<"
        elif char == ">" and inside_tag:
            current_tag += ">"
            tags.append(current_tag)
            current_tag = ""
            inside_tag = False
        elif inside_tag:
            current_tag += char
    return tags
