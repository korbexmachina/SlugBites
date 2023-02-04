"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""
import datetime
monthurslatenight = {
    range(0, 14): "Closed",
    range(14, 22): "Breakfast",
    range(22, 23): "Limited Options",
    range(23, 28): "Lunch",
    range(28, 34): "Limited Options",
    range(34, 40): "Dinner",
    range(40, 46): "Late Night",
    range(46, 48): "Closed"
}

monthursnolatenight = {
    range(0, 14): "Closed",
    range(14, 22): "Breakfast",
    range(22, 23): "Limited Options",
    range(23, 28): "Lunch",
    range(28, 34): "Limited Options",
    range(34, 40): "Dinner",
    range(40, 48): "Closed"
}

fridayearlyEnd = {
    range(0, 14): "Closed",
    range(14, 22): "Breakfast",
    range(22, 23): "Limited Options",
    range(23, 28): "Lunch",
    range(28, 34): "Limited Options",
    range(34, 38): "Dinner",
    range(38, 48): "Closed"
}

satsunearlyEnd = {
    range(0, 14): "Closed",
    range(14, 22): "Breakfast",
    range(22, 28): "Lunch",
    range(28, 34): "Limited Options",
    range(34, 38): "Dinner",
    range(38, 48): "Closed"
}
satsunnormal = {
    range(0, 14): "Closed",
    range(14, 22): "Breakfast",
    range(22, 28): "Lunch",
    range(28, 34): "Limited Options",
    range(34, 40): "Dinner",
    range(40, 48): "Closed"
}

satsunlatenight = {
    range(0, 14): "Closed",
    range(14, 20): "Breakfast",
    range(20, 28): "Lunch",
    range(28, 34): "Limited Options",
    range(34, 40): "Dinner",
    range(40, 46): "Late Night",
    range(46, 48): "Closed"
}

# time is multiplied by 2
times = {
    0: {
        'College Nine/John R Lewis': monthurslatenight,
        'Cowell/Stevenson': monthurslatenight,
        'Crown/Merrill': monthursnolatenight,
        'Porter/Kresge': monthurslatenight
    },
    1: {
        'College Nine/John R Lewis': monthurslatenight,
        'Cowell/Stevenson': monthurslatenight,
        'Crown/Merrill': monthursnolatenight,
        'Porter/Kresge': monthurslatenight
    },
    2: {
        'College Nine/John R Lewis': monthurslatenight,
        'Cowell/Stevenson': monthurslatenight,
        'Crown/Merrill': monthursnolatenight,
        'Porter/Kresge': monthurslatenight
    },
    3: {
        'College Nine/John R Lewis': monthurslatenight,
        'Cowell/Stevenson': monthurslatenight,
        'Crown/Merrill': monthursnolatenight,
        'Porter/Kresge': monthurslatenight
    },
    4: {
        'College Nine/John R Lewis': monthurslatenight,
        'Cowell/Stevenson': monthursnolatenight,
        'Crown/Merrill': monthursnolatenight,
        'Porter/Kresge': fridayearlyEnd
    },
    5: {
        'College Nine/John R Lewis': satsunlatenight,
        'Cowell/Stevenson': satsunnormal,
        'Crown/Merrill': {range(0, 48): "Closed"},
        'Porter/Kresge': satsunearlyEnd
    },
    6: {
        'College Nine/John R Lewis': satsunlatenight,
        'Cowell/Stevenson': satsunlatenight,
        'Crown/Merrill': {range(0, 48): "Closed"},
        'Porter/Kresge': satsunlatenight
    }
}


