systemd-user-session-targets
============================

Provides basic targets and directories for systemd user session.

Each user session daemon that wants to be automatically started in Nemo
user session should do following:

*   provide <my-app>.service file in dir /usr/lib/systemd/user/

*   In that service file have following lines (can have many other options too)

        [Unit]
        After=pre-user-session.target
        [Service]
        ExecStart=/path/to/app-executable
        [Install]
        WantedBy=user-session.target

*   In .spec file have

        Requires: systemd-user-session-targets

    and in install section create link to servive file

        ln -s ../<my-app>.service %{buildroot}%{_libdir}/systemd/user/user-session.target.wants/
