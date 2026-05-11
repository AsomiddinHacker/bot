import pino from 'pino';
import { env } from './env.js';

export const logger = pino({
  name: env.APP_NAME,
  level: env.LOG_LEVEL,
  redact: {
    paths: [
      'req.headers.authorization',
      'req.headers["x-api-key"]',
      'req.headers.cookie',
      'process.env.OPENAI_API_KEY',
      'process.env.SUPABASE_SERVICE_ROLE_KEY',
      'process.env.TELEGRAM_BOT_TOKEN'
    ],
    remove: true
  }
});
