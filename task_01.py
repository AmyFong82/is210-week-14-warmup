#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A subclass of Pet from pet module."""

import pet


class Dog(pet.Pet):
    """A subclass of Pet from pet module."""
    
    def __init__(self, has_shots=False, **kwargs):
        """Constructor for Dog class.

        Args:
            has_shots (bool, optional): Weather the dog has shots.
                                        Default: False.
            **kwargs (dict): Arbitrary arguments dictinary passed in from the
                             parent class (Pet) constructor.

        Attributes:
            has_shots (bool, optional): Weather the dog has shots.
                                        Default: False.
            **kwargs (dict): Arbitrary arguments dictinary passed in from the
                             parent class (Pet) constructor.
        """
        self.has_shots = has_shots
        self.kwargs = pet.Pet.__init__(self, **kwargs)
