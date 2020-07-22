<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <title>My encryption app</title>
    <link rel="stylesheet" type="text/css" href="style.css">
    <link rel="icon" href="icon.ico">
</head>
<body>
    <div id="wrapper">

        <form action="/" method="POST" enctype="multipart/form-data">
            <textarea class="input-fields"
                      id="input-text"
                      name="text"
                      autofocus
                      placeholder="type your text here, enter the secret key and press the button"
                      required></textarea>
            <input class="input-fields" id="input-key" name="key" type="number" placeholder="secret key" required>
            <input class="btn" id="btn-code" name='mode' value="CODE" type="submit">
            <input class="btn" id="btn-decode" name='mode' value="DECODE" type="submit">
        </form>
        %if result is not None:
            <div class="result">
                <p>{{ result }}</p>
            </div>
        %end
    </div>
</body>
</html>