export default [
  {
    files: ['**/*.js'],
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module'
    },
    rules: {
      'no-console': ['warn', { allow: ['error', 'warn'] }],
      'no-unused-vars': ['error', { argsIgnorePattern: '^_' }]
    }
  }
];
