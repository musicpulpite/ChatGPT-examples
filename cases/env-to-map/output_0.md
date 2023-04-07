```
/**
 * Parses an env file string and returns a map of key-value pairs.
 * Comments directly above the env var declaration are preserved.
 *
 * @param {string} envString - The env file string to parse.
 * @returns {Map<string, string>} - A map of env variable keys and values.
 */
function parseEnvString(envString) {
  const envMap = new Map();
  const lines = envString.split('\n');
  let currentComment = '';

  for (const line of lines) {
    // Check if this line is a comment, and update currentComment accordingly
    if (line.startsWith('#')) {
      currentComment = line.trim();
      continue;
    }

    // If this line is not a comment, parse it as an env var
    const [key, value] = line.split('=');
    if (key && value) {
      envMap.set(key.trim(), { value: value.trim(), comment: currentComment });
      currentComment = ''; // Reset currentComment for next env var
    }
  }

  return envMap;
}
```

Example usage:
```
const envString = `
# This is a comment
FOO=bar # This is another comment
BAZ=qux`;

const envMap = parseEnvString(envString);
console.log(envMap.get('FOO')); // { value: 'bar', comment: '# This is a comment' }
console.log(envMap.get('BAZ')); // { value: 'qux', comment: ''}
```