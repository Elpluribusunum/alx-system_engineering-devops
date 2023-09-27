#!usr/bin/env bash
# Making changes to our configuration file with puppet

file { 'ect/ssh/ssh_config':
	ensure => present,

content =>"

	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
