#! /usr/bin/perl
use CGI::Carp 'fatalsToBrowser';
$|=1;

use lib '/home/okazaki_d/perl5/lib/perl5/';
use Text::Markdown 'markdown';

# getの取得
my %get_data = split(/=/,$ENV{'QUERY_STRING'});

# mdファイルをhtmlに変換
open($FILE, $get_data{path});
my @file = <$FILE>;
my $text = join("\n", @file);
my $html = markdown($text);
close ($FILE);

# 表示
print "Content-type:text/html; \n\n";
print $html;

exit;
