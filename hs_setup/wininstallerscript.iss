; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{23340D3E-1854-4A0F-94A1-95D8D8DAFDA2}
AppName=HotSpotter
AppVersion=1
;AppVerName=HotSpotter 1
AppPublisher=Rensselaer Polytechnic Institute
AppPublisherURL=www.rpi.edu/~crallj/
AppSupportURL=www.rpi.edu/~crallj/
AppUpdatesURL=www.rpi.edu/~crallj/
DefaultDirName={pf}\HotSpotter
DefaultGroupName=HotSpotter
OutputBaseFilename=hotspotter-win32-setup
SetupIconFile=C:\Users\jon.crall\code\hotspotter\hs_setup\hsicon.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\jon.crall\code\hotspotter\dist\HotSpotterApp\HotSpotterApp.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\jon.crall\code\hotspotter\dist\HotSpotterApp\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\HotSpotter"; Filename: "{app}\main.exe"
Name: "{commondesktop}\HotSpotter"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\main.exe"; Description: "{cm:LaunchProgram,HotSpotter}"; Flags: nowait postinstall skipifsilent

