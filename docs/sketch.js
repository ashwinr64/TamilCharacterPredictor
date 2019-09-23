const URL = 'http://0.0.0.0:5000/'

function setup() {
  var canvas = createCanvas(256, 256);
  background(255);
  canvas.parent('drawingBoard');
}

function draw() {
  stroke(0);
  strokeWeight(6);
  noFill();
  if (mouseIsPressed === true) {
    line(mouseX, mouseY, pmouseX, pmouseY);
  }
}

$("#predict").click(function () {
  var button = $(this);
  button.html("<i class=\"fas fa-spinner fa-spin\"></i> Predicting");
  button.attr("disabled", true);

  saveFrames('out', 'png', 1, 1, data => {
    payload = JSON.stringify({
      "img": data[0]['imageData']
    });
    $.ajax({
      type: 'POST',
      url: URL,
      headers: {
        'accept': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      data: payload,
      success: function (data) {
        // vals[0] = id && vals[1] = prediction
        vals = Object.values(data);

        $("#predS").html(vals[1]);
        $("#predH").show();
        button.html("Predict");
        button.attr("disabled", false);
      },
      error: function (e) {
        button.html("Predict");
        button.attr("disabled", false);
      },
      dataType: "json",
      contentType: "application/json"
    });
  });
});

$("#reset").click(function () {
  background(255);
  $("#predH").hide();
});
