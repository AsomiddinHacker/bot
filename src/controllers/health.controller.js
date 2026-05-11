import { env } from '../config/env.js';

export function getHealth(req, res) {
  return res.status(200).json({
    success: true,
    data: {
      status: 'ok',
      service: env.APP_NAME,
      env: env.NODE_ENV,
      timestamp: new Date().toISOString(),
      requestId: req.requestId
    }
  });
}
