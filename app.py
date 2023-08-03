# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import numpy as np
import pandas as pd
import openai 
import langchain

from langchain.document_loaders import  TextLoader
from langchain.document_loaders import DirectoryLoader

from langchain.document_loaders import OnlinePDFLoader

from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI



st.title('My app')

