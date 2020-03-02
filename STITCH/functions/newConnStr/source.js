exports = async function(changeEvent) {
  const fullDocument = changeEvent.fullDocument;
  const lambda = context.services.get('aws').lambda("us-east-1");

  const result = await lambda.Invoke({
    FunctionName: "importMongoDS",
    Payload: JSON.stringify({
      "csURI": fullDocument.cs,
      "db": fullDocument.db,
      "col": fullDocument.col,
      "bucket":fullDocument.bucket,
      "dsURI":fullDocument.bucket,
      "fn": fullDocument.fn
    })
  });

  console.log(result.Payload.text());
};
