
# Pyllusion

A Python Module for Generating Visual Illusions

## Installation

    pip install https://github.com/DominiqueMakowski/Pyllusion/zipball/master

## Contribution

You have some ideas? Want to improve things, add new illusions, and help
us shake people’s brain? Let us know, we would be very happy to have you
on board :relaxed:.

## Citation

You can credit the package as follows:

    Makowski, D. (2020). Pyllusion: A Python Module for Generating Visual Illusions. GitHub. 
    Retrieved from https://github.com/DominiqueMakowski/Pyllusion

## Features

### Delboeuf Illusion

The [**Delboeuf
illusion**](https://en.wikipedia.org/wiki/Delboeuf_illusion) is an
optical illusion of relative size perception, where circles of identical
size appear as different. The illusion was named for the Belgian
philosopher, mathematician, experimental psychologist, hypnotist, and
psychophysicist Joseph Remi Leopold Delboeuf (1831–1896), who created it
in 1865.

``` python
import pyllusion as ill

ill.delboeuf_image(illusion_strength=1)
```

![](docs/img/README_delboeuf1.png)

### Autostereograms

[Autostereograms](https://en.wikipedia.org/wiki/Autostereogram) are
images made of a pattern that is horizontally repeated (with slight
variations) which, when watched with the appropriate focus, will
generate an illusion of depth.

For instance, in the image below, the `autostereogram` automatically
adds a guide (you can disable it by setting `guide=False`), the two red
dots. Look at them and relax your eyes until you see a new red dot
between them two. Then, try focusing on this new red dot until it gets
very sharp and until your eyes stabilize. You should then be able to
perceive the letters **3D** as carved in the figure

It can take a bit of time to “get there”, but once you are used to it,
it’s a mind-blowing experience 🤯

``` python
ill.autostereogram(stimulus="3D", width=1600, height=900)
```

![](docs/img/README_autostereogram1.png)

The function is highly customisable, and we can use a black and white
image as a **depth mask** (in this case, the [picture of a
skull](https://github.com/DominiqueMakowski/Pyllusion/docs/img/depthmask.png)
that you will see as emerging from the background), and customise the
pattern used by providing another function (here, the `image_circles()`
function to which we can provide additional arguments like `blackwhite`,
the number of circles `n`, their size range and their transparency with
`alpha`).

``` python
ill.autostereogram(stimulus="docs/img/depthmask.png",
                   pattern=ill.image_circles,
                   blackwhite=True,
                   alpha=0.75,
                   size_min=0.005,
                   size_max=0.03,
                   n=1000)
```

![](docs/img/README_autostereogram2.png)
