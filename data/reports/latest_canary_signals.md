# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T23:22:30.755155+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.04` n `12`; crypto_alt avg `-0.2731` n `234`; crypto_major avg `-0.3916` n `8`; equity avg `0.0298` n `140`; fx avg `-0.0009` n `6`; index avg `0.0025` n `26`; metal avg `-0.0159` n `20`; unknown avg `0.2131` n `944`
- 1h: commodity avg `0.0606` n `12`; crypto_alt avg `0.3583` n `234`; crypto_major avg `-0.0893` n `8`; equity avg `0.2005` n `140`; fx avg `0.0024` n `6`; index avg `0.0277` n `26`; metal avg `0.0606` n `20`; unknown avg `0.3023` n `942`
- 4h: commodity avg `-0.0248` n `12`; crypto_alt avg `0.974` n `234`; crypto_major avg `1.0211` n `8`; equity avg `0.2401` n `140`; fx avg `-0.0136` n `6`; index avg `0.0045` n `26`; metal avg `0.0855` n `20`; unknown avg `-0.1548` n `852`
- 24h: commodity avg `-0.6979` n `12`; crypto_alt avg `4.2273` n `234`; crypto_major avg `6.0926` n `8`; equity avg `2.6897` n `140`; fx avg `-0.1412` n `6`; index avg `0.5535` n `26`; metal avg `0.0953` n `20`; unknown avg `7.6185` n `771`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1754`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
