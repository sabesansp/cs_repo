#!/usr/bin/perl

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
