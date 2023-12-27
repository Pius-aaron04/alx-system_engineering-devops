#executes a program that kills a program

exec{ 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin',
  onlyif  => 'pgrep killmenow',
}
