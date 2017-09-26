<html>
	<head>
	    <script src="http://code.angularjs.org/1.2.13/angular.js"></script>
	    <script src="//cdnjs.cloudflare.com/ajax/libs/angular-ui-router/0.2.8/angular-ui-router.min.js"></script>
		<script type="text/javascript" src="app.js"></script>
	    <script type="text/javascript" src="appConfig.js"></script>
	    <script type="text/javascript" src="appController.js"></script>
	    <script type="text/javascript" src="login/loginController.js"></script>
	    <script type="text/javascript" src="userManagement/userManagementController.js"></script>
	</head>
	<body ng-app="birdView" ng-controller="appController">
		<div>
		    <div ui-view></div>
		</div>
	</body>
</html>