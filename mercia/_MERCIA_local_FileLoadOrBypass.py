# ----------------------------------------------------------------------------

# 
#  \file    _MERCIA_local_FileLoadOrBypass.py
#  \author  glasser
#  \date    2015-07-17
#
#  MERCIA framework

# ----------------------------------------------------------------------------

from mevis import *

def selectChoice():  
  val = ctx.field("Choice").boolValue();
  
  if(val==1):
    ctx.field("Choice2").setBoolValue(0);
    ctx.field("Switch.currentInput").setIntValue(0);
  else:
    ctx.field("Choice2").setBoolValue(1);
    ctx.field("Switch.currentInput").setIntValue(1);
      
  pass


def selectChoice2():  
  val = ctx.field("Choice2").boolValue();
  if(val==1):
    ctx.field("Choice").setBoolValue(0);
    ctx.field("Switch.currentInput").setIntValue(1);
  else:
    ctx.field("Choice").setBoolValue(1);
    ctx.field("Switch.currentInput").setIntValue(0);
  pass