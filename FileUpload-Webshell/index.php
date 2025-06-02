<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>File Upload Lab</title>
  <style>
    body {
      background-color: #f4f6f8;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    .upload-box {
      background-color: #fff;
      padding: 40px;
      border-radius: 12px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.1);
      text-align: center;
      width: 400px;
    }
    h2 {
      color: #2c3e50;
      margin-bottom: 25px;
    }
    input[type="file"] {
      display: block;
      margin: 0 auto 20px auto;
      font-size: 15px;
    }
    input[type="submit"] {
      background-color: #3498db;
      color: white;
      padding: 10px 20px;
      font-size: 15px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    input[type="submit"]:hover {
      background-color: #2980b9;
    }
  </style>
</head>
<body>
  <div class="upload-box">
    <h2>📁 Upload your file</h2>
    <form method="POST" enctype="multipart/form-data" action="upload.php">
      <input type="file" name="file" required><br>
      <input type="submit" value="Upload">
    </form>
  </div>
</body>
</html>