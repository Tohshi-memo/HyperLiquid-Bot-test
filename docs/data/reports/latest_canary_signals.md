# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T21:07:24.815791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0105` n `12`; crypto_alt avg `0.0576` n `232`; crypto_major avg `0.0511` n `8`; equity avg `0.0346` n `134`; fx avg `0.0165` n `6`; index avg `0.0013` n `26`; metal avg `-0.0158` n `20`; unknown avg `0.4145` n `787`
- 1h: commodity avg `-0.0195` n `12`; crypto_alt avg `0.4189` n `232`; crypto_major avg `0.523` n `8`; equity avg `0.0005` n `134`; fx avg `0.0223` n `6`; index avg `0.0083` n `26`; metal avg `-0.0002` n `20`; unknown avg `146.8511` n `781`
- 4h: commodity avg `-0.068` n `12`; crypto_alt avg `0.4968` n `232`; crypto_major avg `0.4977` n `8`; equity avg `0.1794` n `134`; fx avg `0.0298` n `6`; index avg `0.0226` n `26`; metal avg `0.0291` n `20`; unknown avg `0.3458` n `755`
- 24h: commodity avg `-0.0073` n `12`; crypto_alt avg `1.4889` n `232`; crypto_major avg `0.5644` n `8`; equity avg `0.3756` n `134`; fx avg `0.0222` n `6`; index avg `0.0285` n `26`; metal avg `-0.0268` n `20`; unknown avg `106.4289` n `678`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1706`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
