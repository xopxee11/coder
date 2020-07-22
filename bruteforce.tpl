<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <title>My encryption app</title>
    <link rel="stylesheet" type="text/css" href="style.css">
    <link rel="icon" href="icon.ico">
</head>
<style>
    body {
            overflow-y: auto;
    }
</style>
<body>
    <div id="wrapper">

        <form action="/bruteforce" method="POST" enctype="multipart/form-data">
            <textarea class="input-fields"
                      id="input-text"
                      name="message"
                      autofocus
                      placeholder="type your text here, press the button and wait..."
                      required></textarea>
            <input class="btn" id="btn-crack" name='mode' value="CRACK" type="submit">
        </form>
        %if options is not None:
            <div class="result">
                <table>
                    %for option in options:
                        <tr>
                            <td>{{ option }}</td>
                        </tr>
                    %end
                </table>
            </div>
        %end
    </div>
</body>
</html>