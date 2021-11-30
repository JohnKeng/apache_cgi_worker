#!/usr/bin/perl

print "Content-type:text/html\r\n\r\n";
print '<html>';
print '<head>';
print '<title>cgi ENV info</title>';
print '<meta charset="utf-8">';

print '</head>';
print '<body>';
print '<h2>Hello, CGI form Perl Script</h2>';
print '<p>以下為 Perl 腳本調用的環境變量 %ENV </p>';
print '<pre>';
    foreach my $key (keys %ENV) {
        print "$key --> $ENV{$key}<br>";
    }
print '</pre>';
print '</body>';
print '</html>';

1;

