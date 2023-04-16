#!/usr/bin/env python
# -*- coding: utf-8 -*-

import torch
from torchtext.datasets import AG_NEWS 
train_iter = iter(AG_NEWS(split='train'))
