# Make this a part of the package called 'Session'
package Session;

use strict;
use warnings;


# Create a hash called 'cli_param'
# inside the class
sub new 
{

   my $class = shift;
   my $cli_param = shift;
   my $self = {
                 'cli_param' => $cli_param,
              };
   bless ($self,$class);
   return $self;
}

# Sets the cli parameters hash
sub setCliParam
{
   my($self,$cli_param) = @_;
   $self->{'cli_param'} = $cli_param;
}

# Gets the cli parameters hash
sub getCliParam
{
   my $self = shift;
   return $self->{'cli_param'};
}

1;
