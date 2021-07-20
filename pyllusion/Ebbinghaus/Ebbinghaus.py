from .ebbinghaus_image import _ebbinghaus_image
from .ebbinghaus_parameters import _ebbinghaus_parameters
from .ebbinghaus_psychopy import _ebbinghaus_psychopy


class Ebbinghaus:
    """
    A class to generate the Ebbinghaus Illusion.

    The Ebbinghaus illusion is an optical illusion of relative size perception,
    where circles of identical size appear as different because of their
    surrounding context.
    
    Each instance of ``Ebbinghaus`` contains attributes corresponding to the parameters of the illusion.
    These parameters are:
        * ``Difference``: Objective difference in the target features, by modifying ``difference`` of ``ebbinghaus_parameters()``
        * ``Illusion``: Name of the illusion.
        * ``Illusion_Strength``: Strength of the surrounding context in biasing illusion, by modifying ``illusion_strength`` of ``ebbinghaus_parameters()``.
        * ``Illusion_Type``: 'Congruent' if biased towards perceiving the illusion, and 'Incongruent' if against. 
        * ``Size_Min``: size of the smaller inner circle, by modifying ``size_min`` of ``ebbinghaus_parameters()``.
        * ``Size_Inner_Left``: Size of the inner left circle.
        * ``Size_Inner_Right``: Size of the inner right circle.
        * ``Sine_Inner_Difference``: Difference in size (area) of the left and right inner circles.
        * ``Size_Outer_Left``: Size of the surrounding circles around the left inner circle.
        * ``Size_Outer_Right``: Size of the surrounding circles around the right inner circle.
        * ``Distance``: Distance between the circles, by modifying ``distance`` of ``ebbinghaus_parameters()``.
        * ``Distance_Reference``: Distance between circles is computed 'Between Edges' or 'Between Centers', by modifying ``distance_auto`` of ``ebbinghaus_parameters()``.
        * ``Distance_Edges_Inner``: Distance between the edges of the inner left and right circles.
        * ``Distance_Edges_Outer``: Distance between the edges of the surrounding left circles and right circles.
        * ``Size_Inner_Smaller``: Size of the smaller inner circle.
        * ``Size_Inner_Larger``: Size of the larger inner circle.
        * ``Size_Outer_Smaller``: Size of the smaller surrounding circles.
        * ``Size_Outer_Larger``: Size of the larger surrounding cricles.
        * ``Position_Outer_x_Left``: x-coordinates of the left surrounding circles.
        * ``Position_Outer_y_Left``: y-coordinates of the left surrounding circles.
        * ``Position_Outer_x_Right``: x-coordinates of the right surrounding circles.
        * ``Position_Outer_y_Right``: y-coordinates of the right surrounding circles.
        * ``Position_Left``: Position of the left inner circle.
        * ``Position_Right``: Position of the right inner circle.
    """

    def __init__(
        self, illusion_strength=0, difference=0, size_min=0.25, distance=1, distance_auto=False
    ):
        """
        Compute parameters for the Ebbinghaus Illusion.

        Parameters
        ----------
        illusion_strength : float
            The strength of the surrounding context, i.e. outer circles, in biasing perception of unequally sized inner circles.
            Specifically, the size of right outer circles relative to the left (in percentage, e.g, if ``difference=1``,
            it means that the right outer circles will be 100% bigger, i.e., 2 times bigger than the left
            outer circles). A negative sign reflects the size difference of the left outer circles relative
            to the right, i.e., ``difference=-1`` means the left outer circles will be 100% bigger than the
            right outer circles.
        difference : float
            The objective size difference of the inner circles.
            Specifically, the size of left inner circle relative to the right (in percentage, e.g., if ``difference=1``,
            it means that the left inner circle will be 100% bigger, i.e., 2 times bigger than the right).
             A negative sign reflects the size difference of the right inner circle relative to the left, i.e.,
             ``difference=-1`` means the right inner circle will be 100% bigger than the left inner circle.
        size_min : float
            Size of smaller inner circle.
        distance : float
            Distance between circles.
        distance_auto : bool
            If true, distance is between edges (fixed spacing), if false, between centers (fixed location).

        Returns
        -------
        dict
            Dictionary of parameters of the Ebbinghaus illusion.

        Examples
        ---------
        >>> import pyllusion
        >>>
        >>> parameters = pyllusion.ebbinghaus_parameters()
        """
        self.parameters = _ebbinghaus_parameters(
            illusion_strength=illusion_strength,
            difference=difference,
            size_min=size_min,
            distance=distance,
            distance_auto=distance_auto,
        )
    
    def get_parameters(self):
        """
        Returns a dictionary of parameters passed into the Ebbinghaus illusion.
        """
        return self.parameters

    def to_dict(self):
        """
        Alias for `get_parameters()`.
        """
        return self.get_parameters()

    def to_image(self, width=800, height=600, background="white", **kwargs):
        """Create a PIL image of the Ebbinghaus illusion.
    
        Parameters
        ----------
        width : int
            Width of the returned image.
        height : int
            Height of the returned image.
        background : str
            Color of the background.
        **kwargs
            Additional arguments passed into `ebbinghaus_parameters()`.
    
        Returns
        -------
        Image
            Image of the Ebbinghaus illusion, defaults to 800 x 600 pixels.
            Can be resized
            (`resize()`, See https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.resize)
            and saved in different file formats
            (`save()` See https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html).
    
        Examples
        ---------
        >>> import pyllusion
        >>>
        >>> ebbinghaus = pyllusion.Ebbinghaus(illusion_strength=1, difference=2)
        >>> ebbinghaus.to_image()
        """    
        img = _ebbinghaus_image(
            parameters=self.parameters,
            width=width,
            height=height,
            background=background,
            **kwargs
        )
        return img

    def to_psychopy(self, window, **kwargs):
        """Create a PsychoPy stimulus of the Ebbinghaus illusion.

        Parameters
        ----------
        window : object
            The window object initiated by `psychopy.visual.Window` in which the stimulus will be rendered.
        **kwargs
            Additional arguments passed into `ebbinghaus_parameters()`.

        Returns
        -------
        In-place modification of the PsychoPy window (No explicit return).
    
        Examples
        ---------
        >>> import pyllusion
        >>> from psychopy import visual, event
    
        >>> # Create parameters
        >>> ebbinghaus = pyllusion.Ebbinghaus(difference=2, illusion_strength=3)
    
        >>> # Initiate Window
        >>> window = visual.Window(size=[800, 600], winType='pygame', color='white')
    
        >>> # Display illusion
        >>> ebbinghaus.to_psychopy(window)
    
        >>> # Refresh and close window
        >>> window.flip()
        >>> event.waitKeys()  # Press any key to close
        >>> window.close()

        """
        _ebbinghaus_psychopy(window, self.parameters, **kwargs)
