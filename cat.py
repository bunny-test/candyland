class Cat:
    """Represent a cat."""

    def __init__(self, name='cat', color='tabby',
                 * , strength=10, will=10):
        """
        Create cat with name, color, and some stats.
        Stats are keyword-only.
        """
        self.name = name
        self.color = color
        self.strength = strength
        self.will = will

    def drop(self, **kwargs):
        """
        Drop anything given as long as it is not heavy.
        Keyword argument value represent the weight of its keyword.
        """
        things_dropped = [k for k, v in kwargs.items() if v <= self.strength]
        for thing in things_dropped:
            print(f"{self.name.title()} drops {thing}.")
        print(f"Total things dropped: {len(things_dropped)}.")
