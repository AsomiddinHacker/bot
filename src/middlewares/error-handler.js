import { logger } from '../config/logger.js';

export function notFoundHandler(req, res) {
  return res.status(404).json({
    success: false,
    error: {
      code: 'NOT_FOUND',
      message: `Route not found: ${req.method} ${req.originalUrl}`
    }
  });
}

export function errorHandler(err, req, res, next) {
  logger.error({ err, path: req.originalUrl }, 'Unhandled application error');

  return res.status(err.statusCode || 500).json({
    success: false,
    error: {
      code: err.code || 'INTERNAL_SERVER_ERROR',
      message: err.publicMessage || 'An unexpected error occurred'
    }
  });
}
