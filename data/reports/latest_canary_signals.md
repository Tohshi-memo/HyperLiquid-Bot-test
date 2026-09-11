# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T06:07:25.316315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `12`; crypto_alt avg `0.0767` n `233`; crypto_major avg `0.056` n `8`; equity avg `0.1531` n `136`; fx avg `0.0319` n `6`; index avg `0.0232` n `26`; metal avg `0.0635` n `20`; unknown avg `0.0869` n `772`
- 1h: commodity avg `-0.2053` n `12`; crypto_alt avg `0.0476` n `233`; crypto_major avg `0.1662` n `8`; equity avg `0.4699` n `136`; fx avg `0.0124` n `6`; index avg `0.0778` n `26`; metal avg `0.1959` n `20`; unknown avg `0.4531` n `772`
- 4h: commodity avg `-0.39` n `12`; crypto_alt avg `0.7441` n `233`; crypto_major avg `0.5949` n `8`; equity avg `0.4318` n `136`; fx avg `-0.0258` n `6`; index avg `0.1273` n `26`; metal avg `0.3012` n `20`; unknown avg `26.5578` n `760`
- 24h: commodity avg `0.8921` n `12`; crypto_alt avg `-1.5689` n `233`; crypto_major avg `-1.7629` n `8`; equity avg `-1.5809` n `136`; fx avg `0.0829` n `6`; index avg `-0.2694` n `26`; metal avg `-1.0756` n `20`; unknown avg `0.7585` n `685`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
