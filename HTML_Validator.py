#!/bin/python3


def validate_html(html):
    '''
    Thiss function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    try:
        tags = _extract_tags(html)
    except ValueError:
        return False

    stack = []
    for tag in tags:
        if tag.startswith('</'):
            tag_name = tag[2:-1].strip()
            if not stack or stack[-1] != tag_name:
                return False
            stack.pop()
        else:
            tag_content = tag[1:-1].strip()
            tag_name = tag_content.split()[0]
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
            if inside_tag:
                raise ValueError('found < without matching >')
            inside_tag = True
            current_tag.append(char)
        elif char == ">":
            if not inside_tag:
                continue
            current_tag.append(char)
            tags.append("".join(current_tag))
            current_tag = []
            inside_tag = False
        elif inside_tag:
            current_tag.append(char)

    if inside_tag:
        raise ValueError('found < without matching >')

    return tags
