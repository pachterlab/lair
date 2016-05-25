---
layout: page
title: About
permalink: /about/
---

Welcome to the bear's lair!
This website houses a publicly available
database of RNA-seq papers combined with their (re-)analysis performed
using [kallisto](https://pachterlab.github.io/kallisto/) and [sleuth](http://pachterlab.github.io/sleuth/).

You can check out the GitHub for this project at {% include icon-github.html %}[bears_analysis](https://github.com/pachterlab/bears_analyses).

The [Papers](/{{ site.baseurl }}/papers) page contains a basic list of papers
and links to their analysis as well as the meta-data files about those
experiments pulled from the [Short Read Archive](http://www.ncbi.nlm.nih.gov/sra).

Sleuth uses statistical bootstraps to perform differential analysis.
Sleuth pre-computes sufficient statistics from the bootstraps to generate the plots
seen in the analyses, and then abandons the bootstrap data before shipping
the analyses online. Abandoning the bootstrap data drastically cuts down
the file size of sleuth objects, allowing anyone on a laptop to inspect
high-volume RNA-seq datasets.

Making RNA-seq analysis easily accessible online promotes the makes RNA-seq
results more verifiable and reproducible. Furthermore, it allows
others to discover interesting results about an RNA-seq experiment
that may not have been included in the original paper.

<img src="{{ site.baseurl }}/_images/bears_large_compress.jpg">
