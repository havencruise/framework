from django.shortcuts import render
from django.template import RequestContext
from django.conf import settings


def render_template_with_alternates(template, context,
                                    context_instance=None,
                                    request=None):

    if request is not None or context_instance is not None:
        if request is None:     # means we have context_instance
            request = context_instance.get('request', None)

    if not isinstance(template, (list, tuple)):
        template = (template,)

    templates = get_templates_for_request(template, request)

    from django.template.loader import select_template
    from django.template.context import Context
    from copy import copy

    t = select_template(templates)
    ctx = copy(context_instance) if context_instance else Context()
    ctx.update(context)

    return t.render(ctx)


def get_alternate_template_from_request(request):
    if request is not None:
        if hasattr(request, '_use_alternate_template'):
            template = getattr(request, '_use_alternate_template')
            return template
    return None


def get_alternate_template(context_instance):
    """
    Used by device_aware_render_to_response, which gets the name of the
    alternate template string to use from middleware.DeviceTemplateDetect

    """
    request = None

    if context_instance is not None:
        request = context_instance.get('request', None)
        return get_alternate_template_from_request(request)

    return None


def get_templates_for_request(templates, request=None, device_template=None):

    if device_template is None:
        device_template = get_alternate_template_from_request(request)

    if device_template:
        device_templates = []
        for template in templates:
            _template = template.replace('.html', '.%s.html' % device_template)
            device_templates.append(_template)
            device_templates.append(template)

        return device_templates

    return templates


def device_aware_render_to_response(*args, **kwargs):
    """
    Injects device detect template names if settings.DEVICE_TEMPLATE_ENABLED
    before passing to django's render

    See middleware.DeviceTemplateDetect for more information
    """

    if not getattr(settings, 'DEVICE_TEMPLATE_ENABLED', False):
        return render(*args, **kwargs)

    else:
        _device_template = get_alternate_template(
            kwargs.get('context_instance', None))

        if _device_template is None:
            return render(*args, **kwargs)

        _args = [arg for arg in args]
        _template = _args.pop(1)
        _templates = [
            arg for arg in _template if isinstance(_template, (list, tuple))
        ]
        if len(_templates) == 0:
            _templates.append(_template)

        device_templates = get_templates_for_request(
            _templates, device_template=_device_template)

        _args.insert(1, device_templates)
        return render(*_args, **kwargs)


def render_to(template):
    """
    Decorator for Django views that sends returned dict to render function
    with given template and RequestContext as context instance.

    If view doesn't return dict then decorator simply returns output.
    Additionally view can return two-tuple, which must contain dict as first
    element and string with template name as second. This string will
    override template name, given as parameter
    inspired and modified from http://djangosnippets.org/snippets/821/

    Parameters:
     - template: template name to use
    """
    def renderer(func):
        def wrapper(request, *args, **kw):
            if not hasattr(request, 'base_template'):
                setattr(request, 'base_template', 'base.html')
            output = func(request, *args, **kw)
            if isinstance(output, (list, tuple)):
                return device_aware_render_to_response(
                    request, output[1], output[0])
            elif isinstance(output, dict):
                return device_aware_render_to_response(
                    request, template, output)
            return output
        return wrapper
    return renderer
