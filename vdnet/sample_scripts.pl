use strict;
use warnings;

my $input_str = "/f1/dc1";

## print the input string
print "input = ",$input_str,"\n";

## split the string on /
my @split_string = split('/',$input_str);

if($#split_string == 0) {

   print "Invalid datacenter name : need ".
         "to specify the folder as well\n";

} else {


   print "first_string = ",$split_string[0],"\n";
   print "last_string = ",$split_string[2],"\n";

}

## split function

my @temp_ip = split(/\//,"/ser/get");
print "temp ip[1] = ".$temp_ip[1]."\n";
my $size = @temp_ip;
print "size = ".$size; 



