# ----------------------------------------------------------------------------

# 
#  \file    _MERCIA_local_CropROIMacro.py
#  \author  glasser
#  \date    2015-07-18
#
#  MERICA framework

# ----------------------------------------------------------------------------

from mevis import *


def init(*args):
  # init Macro Module
  ctx.field("Bypass1.noBypass").setBoolValue(1)
  #ctx.field("ROISelect.grayCenter").setFloatValue(0.5)
  #ctx.field("ROISelect.grayWidth").setFloatValue(0.1)
  ctx.field("LutWidth").setFloatValue(0.1)
  ctx.field("LUTWidthField.x").setFloatValue(0.1)
  pass

def SelectTab0Function():
  ctx.control("TabViewFor_MERCIA_local_CropROIMacro").selectTabAtIndex(0)
  pass

def SelectTab1Function():
  ctx.control("TabViewFor_MERCIA_local_CropROIMacro").selectTabAtIndex(1)
  pass

def SelectTab2Function():
  ctx.field("Bypass1.noBypass").setBoolValue(0);
  ctx.field("WEMIsoSurface1.startTaskSynchronous").touch()
  ctx.control("TabViewFor_MERCIA_local_CropROIMacro").selectTabAtIndex(2)
  pass

def saveInitialMesh():
  ctx.field("WEMSave2.save").touch()
  pass


def initializeMesh():
  # update iso value the same way as for contour changes
  isoValue = ctx.field("IsoMinValue").doubleValue()
  ctx.field("Calculator.d1").setDoubleValue(isoValue)
  updateCenter()
  pass

def resetContour():
  ctx.field("SoView2DContour.triggerRemoveAll").touch()
  ctx.field("SoView2DContour.triggerAddContour").touch()
  # update density value
  currentDensity = ctx.field("Calculator3.resultScalar1").floatValue()
  ctx.field("SoView2DContour.density").setFloatValue(currentDensity)
  pass

def updateCenter():
  newCenter = ctx.field("LUTCenterFieldFromContour.x").floatValue()
  ctx.field("LUTCenterField.x").setFloatValue(newCenter)
  ctx.field("View3D3.greyCenter").setFloatValue(newCenter)
  print("new center from contour = ", newCenter)
  pass