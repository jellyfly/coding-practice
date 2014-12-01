#!/usr/bin/perl
use warnings;
use strict;

# first create the message
use Email::MIME;
my $message = Email::MIME->create(
	header_str => [
		From 	=> 'mingtan.uw@gmail.com',
		To	=> 'm9tan@uwaterloo.ca',
		Subject	=> 'perl test',
	],
	attributes => {
		encoding => 'quoted-printable',
		charset => 'ISO-8859-1',

	},
	body_str => "Hello World!\n",
);

# send the message 
use Email:MIME;
use Email:MIME::Sender::Simple qw(sendmail);
sendmail($message); 
