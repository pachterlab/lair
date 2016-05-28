---
layout: page
title: About
permalink: /about/
---

This website houses a database providing interactive access to the (re)analysis of
publicly available RNA-Seq data presented in published papers. The resource is powered by [kallisto](https://pachterlab.github.io/kallisto/), [sleuth](http://pachterlab.github.io/sleuth/), the [Snakemake](https://bitbucket.org/snakemake/snakemake/wiki/Home) workflow management system and the [Shiny](http://shiny.rstudio.com) web application framework. GitHub repositories with the source code for the project are located at {% include icon-github.html %}[bears_analysis](https://github.com/pachterlab/bears_analyses) and {% include icon-github.html %}[lair](https://github.com/pachterlab/lair).

The [Analyses]({{ site.baseurl }}/analyses) page contains a list of papers and links to their sleuth-based analysis sites. Each data set in each publication is processed according to a meta-data file located at {% include icon-github.html %}[bears_analysis](https://github.com/pachterlab/bears_analyses) with data automatically downloaded from the [Short Read Archive](http://www.ncbi.nlm.nih.gov/sra). The infrastructure underlying the website is shown in the following workflow:

<img src="{{ site.baseurl }}/_images/workflow.jpg">

This project was developed by [Harold Pimentel](http://pimentel.github.io),
[Pascal Sturmfels](http://psturmfels.github.io) and [Lior Pachter](https://math.berkeley.edu/~lpachter/) with help from the [Pachter Lab](http://pachterlab.github.io).


