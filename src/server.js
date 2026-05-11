import { buildApp } from './app.js';
import { env } from './config/env.js';
import { logger } from './config/logger.js';

const app = buildApp();

const server = app.listen(env.PORT, () => {
  logger.info({ port: env.PORT }, `✅ ${env.APP_NAME} is running`);
});

function shutdown(signal) {
  logger.info({ signal }, 'Shutting down gracefully');
  server.close(() => {
    logger.info('HTTP server closed');
    process.exit(0);
  });
}

process.on('SIGINT', () => shutdown('SIGINT'));
process.on('SIGTERM', () => shutdown('SIGTERM'));
