from django import template

register=template.Library()
@register.filter(name="cut")
def cut(value,arg):
    # """
    # This function replaces the arg in value with spaces or it cuts args from the value
    # """
    return value.replace(arg,' ')

# register.filter('cut',cut)#filter name,function name
# use any of above two to register the filter
