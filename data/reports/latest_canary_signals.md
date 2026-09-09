# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T02:37:30.576491+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0209` n `12`; crypto_alt avg `0.1052` n `233`; crypto_major avg `0.1465` n `8`; equity avg `0.0899` n `134`; fx avg `0.0174` n `6`; index avg `0.0158` n `26`; metal avg `-0.0292` n `20`; unknown avg `0.0093` n `797`
- 1h: commodity avg `0.0002` n `12`; crypto_alt avg `-0.136` n `233`; crypto_major avg `0.0436` n `8`; equity avg `-0.0049` n `134`; fx avg `0.0312` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0767` n `20`; unknown avg `-0.1459` n `795`
- 4h: commodity avg `0.019` n `12`; crypto_alt avg `-0.1605` n `233`; crypto_major avg `0.3101` n `8`; equity avg `0.5322` n `134`; fx avg `0.0174` n `6`; index avg `0.1258` n `26`; metal avg `0.081` n `20`; unknown avg `0.4861` n `789`
- 24h: commodity avg `0.1617` n `12`; crypto_alt avg `-0.9988` n `232`; crypto_major avg `0.3741` n `8`; equity avg `0.3617` n `134`; fx avg `0.1008` n `6`; index avg `-0.1642` n `26`; metal avg `-0.3468` n `20`; unknown avg `0.7777` n `683`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
