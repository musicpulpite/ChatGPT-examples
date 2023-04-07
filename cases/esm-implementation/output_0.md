Here's an example of how to use the `esm` npm package to execute an ES module with top-level await that imports the `aws-sdk` S3 client to fetch from an S3 bucket:

First, install the `esm` npm package and the `aws-sdk` npm package:

```
npm install esm aws-sdk
```

Next, create an ES module that imports the `aws-sdk` S3 client and fetches an object from an S3 bucket:

```js
// s3-fetch.js

import AWS from 'aws-sdk';

const s3 = new AWS.S3();

export const getObjectFromS3 = async (bucket, key) => {
  const params = {
    Bucket: bucket,
    Key: key,
  };
  const data = await s3.getObject(params).promise();
  return data.Body.toString('utf-8');
};
```

The `getObjectFromS3` function takes two parameters, the name of the S3 bucket and the key of the object to fetch. It returns a promise that resolves with the body of the fetched object as a string.

Now, create a predev script in your `package.json` that executes the ES module with top-level await using the `esm` package:

```json
{
  "scripts": {
    "predev": "node -r esm s3-fetch.js"
  }
}
```

The `-r esm` option tells Node.js to use the `esm` package to load and execute the module.

Finally, to use the authentication credentials from the result of `aws sso login`, configure the `AWS` object with the credentials:

```js
// index.js

import AWS from 'aws-sdk';
import { getObjectFromS3 } from './s3-fetch.js';

// Configure AWS with the credentials from `aws sso login`
AWS.config.credentials = new AWS.ProcessCredentials({
  roleArn: '<SSO_ROLE_ARN>',
  webIdentityToken: '<SSO_ACCESS_TOKEN>',
  region: '<AWS_REGION>'
});

(async () => {
  // Fetch the object from the S3 bucket
  const bucket = 'my-bucket';
  const key = 'path/to/object.txt';
  const data = await getObjectFromS3(bucket, key);
  console.log(data);
})();
```

Replace `<SSO_ROLE_ARN>`, `<SSO_ACCESS_TOKEN>`, and `<AWS_REGION>` with the appropriate values from the output of `aws sso login`.

This example code can be used by a professional software engineer and can be easily extended to use different AWS SDK services and methods.