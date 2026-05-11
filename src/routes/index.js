import { Router } from 'express';
import { healthRouter } from './v1/health.routes.js';

const router = Router();
router.use('/v1', healthRouter);

export { router };
