cmake_minimum_required(VERSION 3.0)

project(ddpm LANGUAGES NONE)

install(PROGRAMS ddpm.py
	RENAME ddpm
	DESTINATION bin
)

install(PROGRAMS dolcesdk-update.py
	RENAME dolcesdk-update
	DESTINATION bin
)

install(PROGRAMS dolcesdk-update-packages.py
	RENAME dolcesdk-update-packages
	DESTINATION bin
)
