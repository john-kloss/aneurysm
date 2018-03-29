# ----------------------------------------------------------------------------

# 
#  \file    MERCIA_local.py
#  \author  glasser
#  \date    2015-07-17
#
#  MERCIA_local_2 framework

# ----------------------------------------------------------------------------

from mevis import *

def init(*args):
  # init the Macro Module -> set all bypasses to "no bypass"
  ctx.field("BypassAfterLoadMacro.noBypass").setBoolValue(1)
  ctx.field("BypassAfterCropROIMacro.noBypass").setBoolValue(1)
  # ctx.field("BypassAfterCropWEMMacro.noBypass").setBoolValue(1)

  pass

def SelectTabTitleFunction():
  ctx.control("MERCIA_MainFrame").selectTabAtIndex(3)
  ctx.field("BypassAfterLoadMacro.noBypass").setBoolValue(1)
  pass

def SelectTab1Function():
  ctx.control("MERCIA_MainFrame").selectTabAtIndex(0)
  ctx.field("BypassAfterLoadMacro.noBypass").setBoolValue(1)
  pass

def SelectTab2Function():
  ctx.control("MERCIA_MainFrame").selectTabAtIndex(1)
  ctx.field("BypassAfterLoadMacro.noBypass").setBoolValue(0)
  ctx.field("BypassAfterCropROIMacro.noBypass").setBoolValue(1)
  pass

def SelectTabWEMCutFunction():
  ctx.control("MERCIA_MainFrame").selectTabAtIndex(2)
  ctx.field("BypassAfterCropROIMacro.noBypass").setBoolValue(0)
  pass
 
def SelectTab3Function():
  ctx.control("MERCIA_MainFrame").selectTabAtIndex(3)
  ctx.field("BypassAfterCropROIMacro.noBypass").setBoolValue(0)
  ctx.field("BypassAfterCropWEMMacro.noBypass").setBoolValue(1)
  pass

def SelectTab4Function():
  ctx.control("MERCIA_MainFrame").selectTabAtIndex(4)
  ctx.field("BypassAfterCropWEMMacro.noBypass").setBoolValue(0)
  pass

def SelectTab5Function():
  ctx.control("MERCIA_MainFrame").selectTabAtIndex(5)
  ctx.field("BypassAfterLocallySmoothMacro.noBypass").setBoolValue(1)
  pass

def SelectTab6Function():
  ctx.control("MERCIA_MainFrame").selectTabAtIndex(6)
  ctx.field("BypassAfterLocallySmoothMacro.noBypass").setBoolValue(0)
  pass

def SelectTab7Function():
  ctx.control("MERCIA_MainFrame").selectTabAtIndex(7)
  pass

def SelectTab8Function():
  ctx.control("MERCIA_MainFrame").selectTabAtIndex(8)
  pass

def SelectTab9Function():
  ctx.control("MERCIA_MainFrame").selectTabAtIndex(9)
  pass