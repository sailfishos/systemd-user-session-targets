systemd-user-session-targets
============================

Provides basic targets and directories for systemd user session.
Each user session daemon that wants to be automatically started in Nemo
user session should do following:

1) provide <my-app>.service file in dir /usr/lib/systemd/user/

2) In that service file have following lines (can have many other options too)
[Unit]
After=pre-user-session.target
[Service]
ExecStart=/path/to/app-executable
[Install]
WantedBy=user-session.target

4) In .spec file have
Requires: systemd-user-session-targets
and in install section create link to servive file
ln -s ../<my-app>.service /usr/lib/systemd/user/user-session.target.wants/
