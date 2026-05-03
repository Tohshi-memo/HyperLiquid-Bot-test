# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T22:21:59.513121+00:00`
- Correlation status: `ready`
- Asset price records: `208`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.4514` n `7`; crypto_alt avg `0.3769` n `223`; crypto_major avg `0.4505` n `7`; equity avg `-0.0289` n `42`; fx avg `-0.0053` n `4`; index avg `-0.2571` n `9`; metal avg `0.0049` n `7`; unknown avg `0.0777` n `314`
- 1h: commodity avg `0.4471` n `7`; crypto_alt avg `0.289` n `223`; crypto_major avg `0.4199` n `7`; equity avg `0.0111` n `42`; fx avg `-0.009` n `4`; index avg `-0.0531` n `9`; metal avg `-0.2233` n `7`; unknown avg `0.2313` n `314`
- 4h: commodity avg `-0.0255` n `7`; crypto_alt avg `0.5547` n `223`; crypto_major avg `0.6392` n `7`; equity avg `0.2431` n `42`; fx avg `-0.0448` n `4`; index avg `0.0222` n `9`; metal avg `-0.1204` n `7`; unknown avg `0.1998` n `314`
- 24h: commodity avg `-0.1637` n `7`; crypto_alt avg `0.0806` n `223`; crypto_major avg `0.5598` n `7`; equity avg `0.2862` n `42`; fx avg `-0.0283` n `4`; index avg `0.062` n `9`; metal avg `0.3719` n `7`; unknown avg `0.1986` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3933`, n `204`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3909`, n `200`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3862`, n `200`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3759`, n `204`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.355`, n `204`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3426`, n `204`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3015`, n `204`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2922`, n `204`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.2819`, n `204`, moderate_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.2331`, n `204`, weak_sample_signal
