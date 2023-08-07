#Author-schneik
#Description-Displays a Document's URN, Parent Folder, Project, and Hub data

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    _ui = None
    try:

        _app = adsk.core.Application.get()
        _ui  = _app.userInterface

        # Check that the active document has been saved.
        doc = _app.activeDocument
        if not doc.isSaved:
            _ui.messageBox('The active document must be saved before running this script.')
            return

        docHub = _app.data.activeHub.id
        docHubName = _app.data.activeHub.name

        docProject = _app.data.activeProject.id
        docProjectName = _app.data.activeProject.name

        docFolder = _app.activeDocument.dataFile.parentFolder.id
        if docProjectName == _app.activeDocument.dataFile.parentFolder.name:
            docFolderName = "Project Root"
        else:
            docFolderName= _app.activeDocument.dataFile.parentFolder.name    
        
        docID = _app.activeDocument.dataFile.id
        docName = _app.activeDocument.dataFile.name

        resultString = "<b>Team HUB Name:</b> " + docHubName + "<br>" + "<b>Team HUB ID</b>: " + docHub + "<p>" + "<b>Project Name</b>: " + docProjectName + "<br>" + "<b>Project ID:</b> " + docProject + "<p>" + "<b>Parent Folder Name:</b> " + docFolderName + "<br>" + "<b>Parent Folder ID:</b> " + docFolder + "<p>" + "<b>Document Name:</b> " + docName + "<br>" + "<b>Document ID:</b> " + docID

        _ui.messageBox(resultString)

    except:
        if _ui:
            _ui.messageBox('Failed:<br>{}'.format(traceback.format_exc()))
