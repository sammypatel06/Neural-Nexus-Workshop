// adversarial-example/functions/predict.js
const tf = require("@tensorflow/tfjs-node");
const sharp = require("sharp");
const path = require("path");

// ---- 1. Model loading -----------------------------------------
const MODEL_JSON_PATH = path.join(
  __dirname,
  "..",
  "public",
  "key_model",
  "model.json",
);
let modelPromise = null;
async function loadModel() {
  if (!modelPromise) {
    const absPath = `file://${MODEL_JSON_PATH}`;
    modelPromise = tf.loadGraphModel(absPath);
  }
  return modelPromise;
}

// ---- 2. Image preprocessing -----------------------------------
async function preprocess(buffer) {
  // Resize to the size your model expects – adjust if needed
  return tf.node
    .decodeImage(buffer)
    .resizeNearestNeighbor([128, 128])
    .toFloat()
    .div(tf.scalar(255.0))
    .expandDims(); // add batch dim
}

// ---- 3. Lambda handler -----------------------------------------
exports.handler = async function (event, context) {
  try {
    // ---- parse body -----------------------------------------
    let imageBuffer;
    const ct = event.headers["content-type"] || event.headers["Content-Type"];

    if (ct && ct.includes("multipart/form-data")) {
      // Very minimal multipart parsing – for production use busboy/multer
      const boundary = ct.split("boundary=")[1];
      const parts = Buffer.from(event.body, "base64")
        .toString()
        .split(`--${boundary}`);
      const filePart = parts.find((p) =>
        p.includes('Content-Disposition: form-data; name="file"'),
      );
      if (!filePart) throw new Error("Missing file field");
      const [, , , base64] = filePart.split("\r\n\r\n");
      imageBuffer = Buffer.from(base64.trim(), "base64");
    } else {
      // JSON body
      const { image } = JSON.parse(event.body);
      if (!image) throw new Error("Missing image");
      imageBuffer = Buffer.from(image, "base64");
    }

    // ---- run inference ----------------------------------------
    const model = await loadModel();
    const inputTensor = await preprocess(imageBuffer);
    const logits = model.predict(inputTensor);

    // Assume binary sigmoid output (single value)
    const prob = Array.isArray(logits.dataSync())
      ? logits.dataSync()[0]
      : (await logits.array())[0];

    const confidence = Math.min(Math.max(prob, 0), 1);
    const prediction = confidence >= 0.5 ? "positive" : "negative";

    // ---- optional flag reveal ----------------------------------
    const response = { confidence, prediction };
    if (confidence >= 0.75) {
      response.flag = "FLAG{KEY}";
    }

    return { statusCode: 200, body: JSON.stringify(response) };
  } catch (err) {
    console.error(err);
    return { statusCode: 400, body: JSON.stringify({ error: err.message }) };
  }
};
