#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Shopping list calculator."""

from data import FRUIT


def get_cost_per_item(shoplist):
    """Calculates the total cost per item.

    Args:
        shoplist (dict): A dictionary keyed by the item name and with the values
                         being the number of each item to purchase.

    Returns:
        dict: Keyed by the item name, with values being total cost of each item,
              provided that the item is found in the FRUIT dictionary from data.

    Examples:
        >>> shoplist = {'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}
        >>> get_cost_per_item(shoplist)
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    frs = FRUIT
    return {fr: un * frs[fr] for fr, un in shoplist.iteritems() if fr in frs}


def get_total_cost(shoplist):
    """Calculates the total cost of the shopping list.

    Args:
        shoplist (dict): A dictionary keyed by the name of fruit, with the
                         values being the number of units to purchase.

    Returns:
        float: the total cost of the shopping list.

    Examples:
        >>> get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        112.80000000000001
    """
    return sum(value for value in get_cost_per_item(shoplist).itervalues())
