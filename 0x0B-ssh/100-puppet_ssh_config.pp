#!/usr/bin/env bash
# make changes to config file using Puppet

File_line { 'Refuse to authenticate using a password':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}

File_line { 'Use private key':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school'
}
