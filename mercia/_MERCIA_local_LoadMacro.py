# ----------------------------------------------------------------------------

# 
#  \file    _MERCIA_local_LoadMacro.py
#  \author  glasser
#  \date    2015-07-17
#
#  MERCIA framework

# ----------------------------------------------------------------------------

from mevis import *

# --- DICOM Import

# Open Import Dicom dialog
def ImportDialog ():
  importPath = ctx.field("OpenImage.previewName").stringValue()
  if importPath:
    importPath = MLABFileManager.splitPath(importPath)["dir"]
  else:
    importPath = ctx.field("OpenImage.browserRootPath").stringValue()
  ctx.field("OpenImage.import.target").setStringValue(importPath)
  ctx.module("OpenImage.import").showModalDialog()
  return