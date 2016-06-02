#! /usr/bin/perl
use CGI::Carp 'fatalsToBrowser';
$|=1;

# ファイルの取得
my $dir, $num = 0;
while(<./files/*>){

    ## サブディレクトリも読み取れるようにする

    $num++;
    # mdファイルのみ取得
    if(/.*.md/){
        $dir .= "<tr><td>$num</td><td><a href=\"reader.cgi?path=$_\">$_</a></td></tr>";
    }
}

# 表示
my $FH;
open($FH,"view.html");

print "Content-type:text/html; \n\n";
while(!eof($FH)){
    my $line = <$FH>;
    $line =~s/__DIR__/$dir/g;
    print $line;
}

close($FH);

exit;
