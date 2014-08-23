use strict;
use warnings;
use Getopt::Long;
use Data::Dumper;

use Session;
# Declare a variable cli_param that is a 
# hash reference
my $cli_param = {};


# Get the option as a command line parameter
# Use an option like "file_name"  
print GetOptions('file_name|file_name=s' => \$cli_param->{file_name})."\n";

# Print the hash
print "cli_param = ".Dumper($cli_param)."\n";

# Create an object for Session without passing any parameter
my $session = Session->new();

# Print the cli parameters before and after the assignment
print "cli parameters hash in session object before assignment = " .Dumper($session->getCliParam()) ."\n";
$session->setCliParam($cli_param);
print "cli parameters hash in session object after assignment = ".Dumper($session->getCliParam())."\n";





