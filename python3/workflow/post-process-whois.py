    """ An example of using module importation from a post-process script.
    Post-process scripts are used for dealing with the outputs of a function and preparing ways to present the information
    such as creating notes, updating datatables and adding artifacts
    This example shows how we can streamline the fn_whois app with the inclusion of module imports
   """


# try:
#   des = artifact.description.content
# except Exception:
#   des = None

# try:
#   if results["success"]:
#     if des is None:
#       note = u"""<div><p><br><b>RDAP threat intelligence at {2}:</b></br>\n\n
#       <br><b>{0}</b></br></div></p>\n\n
#       <div><p><br><b> Possible accessible keys:</b></br>\n\n
#       <br><b>{1}</b></br>\n\n""".format(results["content"]["display_content"],results["content"].keys(),results["metrics"]["timestamp"])
#       artifact.description = helper.createRichText(note)
#       incident.addNote(helper.createRichText(note))
#     else:
#       note =u"""<div><p><br><b>RDAP threat intelligence at {2}:</b></br>\n\n
#       <br><b>{0}</b></br></div></p>\n\n
#       <div><p><br><b> Possible accessible keys:</b></br>\n\n
#       <br><b>{1}</b></br>\n\n""".format(results["content"]["display_content"],results["content"].keys(),results["metrics"]["timestamp"]) + des
#       artifact.description = helper.createRichText(note)
#       incident.addNote(helper.createRichText(note))
#   else:
#     note = u"""RDAP threat intelligence at {}:\n\n  This Artifact has no ans accessible registry information, \n\n so no intelligence was gathered.  \n\n""".format(results["metrics"]["timestamp"])
#     artifact.description = helper.createRichText(note)
# except:
#   note =  u"""RDAP threat intelligence at {}:\n\n  This Artifact has no ans accessible registry information, \n\n so no intelligence was gathered.  \n\n""".format(results["metrics"]["timestamp"])
#   artifact.description = helper.createRichText(note)


import collections
import json 
from bs4 import BeautifulSoup

pretty_print_keys = ""
for resultkey, val in json.loads(results["content"]["display_content"]).items():
  pretty_print_keys = pretty_print_keys + "<b>{}</b>: {}<br>".format(resultkey, val)

rawText = """<b> RDAP Threat intelligence at {}:</b>
            <p>{}</p>
            <br><b> Possible accessible keys:</b>\n\n
            <br>{}""".format(results["metrics"]["timestamp"],pretty_print_keys,results["content"].keys())

if not results["success"]: # if the function did not get results
  rawText =  u"""RDAP threat intelligence at {}:\n\n  This Artifact has no ans accessible registry information, \n\n so no intelligence was gathered.  \n\n""".format(results["metrics"]["timestamp"])
  artifact.description = helper.createRichText(note)

soupText = BeautifulSoup(rawText)
incident.addNote(helper.createRichText(soupText.prettify()))