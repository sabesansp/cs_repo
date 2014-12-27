# dependencies on libraries

use YAML qw(LoadFile);
use Data::Dumper;


# execution code here

my $yamlFile = "yaml/person.yaml";
my $yamlHash = LoadFile($yamlFile);
print Data::Dumper->Dump([$yamlHash],
                         [qw(*yamlHash)]);



