# Author-schneik
# Description-Displays a Document's URN, Parent Folder, Project, and Hub data

import adsk.core, adsk.fusion, adsk.cam, traceback


def run(context):
    _ui = None
    try:
        _app = adsk.core.Application.get()
        _ui = _app.userInterface

        # Check that the active document has been saved.
        doc = _app.activeDocument
        if not doc.isSaved:
            _ui.messageBox(
                "The active document must be saved before running this script."
            )
            return

        docHub = _app.data.activeHub.id
        docHubName = _app.data.activeHub.name

        docProject = _app.activeDocument.dataFile.parentProject.id
        docProjectName = _app.activeDocument.dataFile.parentProject.name

        docFolder = _app.activeDocument.dataFile.parentFolder.id
        if _app.activeDocument.dataFile.parentFolder.isRoot == True:
            docFolderName = "Project Root"
        else:
            docFolderName = _app.activeDocument.dataFile.parentFolder.name

        rootTest = _app.activeDocument.dataFile.parentFolder
        docPath = f"{_app.activeDocument.dataFile.parentFolder.name}"
        while rootTest.isRoot == False:
            nextFolder = rootTest.parentFolder.name
            docPath = f"{nextFolder} / {docPath}"
            rootTest = rootTest.parentFolder

        docPath = f"{docPath} / {_app.activeDocument.dataFile.name}"
        docID = _app.activeDocument.dataFile.id
        docName = _app.activeDocument.dataFile.name
        docVersion = _app.activeDocument.dataFile.versionNumber
        docVersions = _app.activeDocument.dataFile.latestVersionNumber
        # docVersionUser = _app.activeDocument.dataFile.lastUpdatedBy.displayName
        docVersionComment = _app.activeDocument.dataFile.description
        docVersionBuild = _app.activeDocument.version
        appVersionBuild = _app.version

        resultString = (
            f"<b>Team HUB Name:</b> {docHubName} <br>"
            f"<b>Team HUB ID:</b> {docHub} <p>"
            f"<b>Project Name:</b> {docProjectName} <br>"
            f"<b>Project ID:</b> {docProject} <p>"
            f"<b>Parent Folder Name:</b> {docFolderName} <br>"
            f"<b>Parent Folder ID:</b> {docFolder} <p>"
            f"<b>Path:</b> {docPath} <p>"
            f"<b>Document Name:</b> {docName} <br>"
            f"<b>Document ID:</b> {docID}<br>"
            f"<b>Document Version:</b> Version {docVersion} of {docVersions}<br>"
            # f"<b>Last Saved By:</b> {docVersionUser}<br>"
            f"<b>Version Comment:</b> ''{docVersionComment}''<br>"
            f"<b>Version Build:</b> Saved by Fusion build {docVersionBuild} (current build is {appVersionBuild})"
        )

        _ui.messageBox(resultString)

    except:
        if _ui:
            _ui.messageBox("Failed:<br>{}".format(traceback.format_exc()))
