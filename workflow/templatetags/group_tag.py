#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.contrib.auth.models import Group

from django import template
from django.template.defaultfilters import stringfilter

from workflow.models import ActivityUserOrganizationGroup

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False


@register.filter(name='has_org_access')
def has_access(activity_user, group):
    user_org_access = ActivityUserOrganizationGroup.objects.filter(
        activity_user_id=activity_user.id,
        organization_id=activity_user.organization.id
    ).first()

    user_group = Group.objects.get(name=user_org_access.group.name)
    if group == user_group.name:
        return True
    return False


@register.filter(name='get_group_name')
def get_group_name(activity_user):
    if activity_user is not None:
        user_org_access = ActivityUserOrganizationGroup.objects.filter(
            activity_user_id=activity_user.id,
            organization_id=activity_user.organization.id).first()
        if user_org_access is not None:
            try:
                return user_org_access.group.name
            except AttributeError:
                return 'Not Set'
    return 'Not Set'


@register.filter
@stringfilter
def template_exists(template_name="links.html"):
    try:
        template.loader.get_template(template_name)
        return True
    except template.TemplateDoesNotExist:
        return False


@register.filter(name='enabled_in_org')
def enabled_in_org(activity_user, organization_id):
    """
    check if a user status is active on an org
    :param activity_user:
    :param organization_id:
    :return: boolean
    """
    user_active_org_access = ActivityUserOrganizationGroup.objects.filter(
        activity_user_id=activity_user.id,
        organization_id=organization_id,
        is_active=True
    ).first()

    if user_active_org_access is not None:
        return True

    return False
