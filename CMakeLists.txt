cmake_minimum_required(VERSION 3.0)

project(ddpm LANGUAGES NONE)

install(PROGRAMS ddpm.sh
	RENAME ddpm
	DESTINATION bin
)

install(PROGRAMS dolcesdk-update.sh
	RENAME dolcesdk-update
	DESTINATION bin
)

install(PROGRAMS dolcesdk-update-packages.sh
	RENAME dolcesdk-update-packages
	DESTINATION bin
)

install(PROGRAMS
	include/install-dolcesdk.sh
	include/install-packages.sh
	DESTINATION bin/include
)
