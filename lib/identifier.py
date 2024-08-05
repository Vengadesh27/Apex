# Copyright (c) 2024 Your Name or Organization
# All rights reserved.
#
# This file is part of the YourFramework project.
#
# Licensed under the MIT License. See LICENSE file in the root of the project for details.
#
# Description:
# This module defines the Generator class used to generate unique 6-character alphanumeric strings.
# These strings can be used for identifying or referencing widgets within the framework.

import string
import random

class Generator:
    def __init__(self):
        # Initialize the Generator instance
        # No specific initialization needed here currently
        self.key()  # Generate a key upon initialization (not typically required in __init__)
        pass

    def key(self):
        """
        Generate a unique 6-character alphanumeric string.
        
        Returns:
            str: A 6-character string consisting of uppercase letters and digits.
        """
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        print(ran)
        return str(ran)
