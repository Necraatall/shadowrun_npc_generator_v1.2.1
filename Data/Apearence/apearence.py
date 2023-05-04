import random
from enum import Enum

eye_color = ('brown', 'black', 'blue', 'green', 'yellow')
hair_color = ('auburn', 'brown', 'black', 'blonde', 'copper', 'ginger', 'golden', 'grey', 'mouse', 'red', 'dark brown', 'white')
skin_tone = ('almond', 'brown', 'bronze', 'chocolate', 'cocoa', 'dark chocolate', 'fair', 'light', 'olive', 'pale', 'walnut')


class Height(Enum):
    VERY_TALL_HEIGHT = "very tall"
    TALL_HEIGHT = "tall"
    AVERAGE_HEIGHT = "average height"
    SHORT_HEIGHT = "short"
    VERY_SHORT_HEIGHT = "very short"


class Weight(Enum):
    VERY_OVERWEIGHT_WEIGHT = "very overweight"
    OVERWEIGHT_WEIGHT = "overweight"
    AVERAGE_WEIGHT = "average weight"
    UNDERWEIGHT_WEIGHT = "underweight"
    VERY_UNDERWEIGHT_WEIGHT = "very underweight"
    BIG_WEIGHT = "big"
    HEAVYSET_WEIGHT = "heavyset weight"
    THIN_WEIGHT = "thin weight"


make_list = list(Weight)
WEIGHT = random.choice(make_list)
WEIGHT = (WEIGHT.value)

age_appearance = random.randrange(0, 2, 1)
physical_age = random.randrange(6, 60, 1)
psychical_age = 0
if age_appearance == 0:
    psychical_age = random.randrange((physical_age // 2), (physical_age - (physical_age // 4) + 1), 1)
    appearence_age = random.randrange((physical_age // 2), (physical_age - (physical_age // 3) + 1 + 3), 1)
else:
    psychical_age = random.randrange((physical_age // 2), (physical_age + (physical_age // 4) - 1), 1)
    appearence_age = random.randrange((physical_age // 2), (physical_age + (physical_age // 3) - 1 + 3), 1)


class Age(Enum):
    PHYSICAL_AGE = physical_age
    PSYCHICAL_AGE = psychical_age
    APPEARENCE_AGE = appearence_age


class Body(Enum):
    VERY_WELL_BUILT_BODY = "very well-built"
    WELL_BUILD_BODY = "well-built"
    AVERAGE_BUILD_BODY = "average build"
    FINE_BUILD_BODY = "fine build"
    VERY_FINE_BUILD_BODY = "very fine build"
    SKINNY_BUILD_BODY = "skinny build"
    SLENDER_BUILD_BODY = "slender build"


make_list = list(Body)
BODY = random.choice(make_list)
BODY = (BODY.value)


class Body_shape(Enum):
    BOTTOM_HOURGLASS = "bottom hourglass"
    INVERTED_TRINGLE = "inverted tringle"
    DIAMOND = "diamond"
    ATHLETIC = "athletic"
    ROUND = "round"
    RECTANGLE = "rectangle"
    TRIANGLE = "triangle"
    HOURGLASS = "hourglass"
    PEAR = "pear"
    APPLE = "apple"
    TRAPEZOID = "trapezoid"


make_list = list(Body_shape)
BODY_SHAPE = random.choice(make_list)
BODY_SHAPE = (BODY_SHAPE.value)
