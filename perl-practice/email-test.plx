#!/usr/bin/perl
use MIME::Lite;
 
$to = 'mingtan.uw@gmail.com';
$cc = 'mingtan.uw@gmail.com';
$from = 'mingtan.uw@gmail.com';
$subject = 'Test Email';
$message = 'This is test email sent by Perl Script';

$msg = MIME::Lite->new(
                 From     => $from,
                 To       => $to,
                 Cc       => $cc,
                 Subject  => $subject,
                 Data     => $message
                 );
                 
$msg->send;
print "Email Sent Successfully\n";
