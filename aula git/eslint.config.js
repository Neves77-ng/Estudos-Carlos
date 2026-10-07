module.exports = [
  {
    files: ["src/**/*.js"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module"
    },
    rules: {
      semi: ["error"],
      "no-unused-vars": "error"
    }
  }
];