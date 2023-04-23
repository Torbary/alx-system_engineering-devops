# execute a command

exec { 'pkill killmenow' :
    path    => '/bin/',
    command => 'pkill killmenow',
    }
