#!/usr/bin/perl

use YAML::XS qw {Dump Load LoadFile DumpFile};
use Getopt::Long;
use Getopt::Std;
use Data::Dumper;
use strict;
use warnings;

my $array =  [];


my $result = $array;


#print(@$array."\n");

if(@$result == 0) {

   print("Empty array\n");
}
else {

   print("Not equal\n");

}

my $hash={"me" =>{} };
my $key="you";

if(ref($hash->{$key}) eq "HASH") {

   print("Hash and key are defined\n");

} else {

   print("Hash and key not defined\n");
}
my $vdnetsrc="scm-trees.eng.vmware.com";
my $vdnetshare = "/trees/vdnet/automation";
my $folder = "f";
print("mount point : $vdnetsrc:$vdnetshare/$folder\n");
my $check_defined;
if(defined $check_defined && $check_defined eq "failure") {

   print("check_defined variable is defined\n");

} else {

   print("check_defined variable is not defined\n");

}
foreach my $item(@ARGV) {
   print("$item\n");
}
my $cli = {};
GetOptions("this|this=s" => \$cli->{"this"},
           "that|that=s" => \$cli->{"that"});

# print the hash cli
print("The cli = " .Dumper($cli)." \n");


	 
