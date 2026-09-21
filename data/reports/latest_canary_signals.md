# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T19:07:34.415756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `-0.2851` n `234`; crypto_major avg `-0.2551` n `8`; equity avg `0.0223` n `140`; fx avg `0.0053` n `6`; index avg `-0.0007` n `26`; metal avg `-0.0272` n `20`; unknown avg `-0.0439` n `940`
- 1h: commodity avg `-0.0158` n `12`; crypto_alt avg `-0.0206` n `234`; crypto_major avg `0.1808` n `8`; equity avg `0.2259` n `140`; fx avg `0.0176` n `6`; index avg `0.0442` n `26`; metal avg `0.0168` n `20`; unknown avg `-0.1632` n `940`
- 4h: commodity avg `-0.0073` n `12`; crypto_alt avg `-1.1522` n `234`; crypto_major avg `-0.184` n `8`; equity avg `0.5897` n `140`; fx avg `-0.0034` n `6`; index avg `0.1501` n `26`; metal avg `-0.0014` n `20`; unknown avg `-0.4925` n `928`
- 24h: commodity avg `-0.9839` n `12`; crypto_alt avg `3.8249` n `234`; crypto_major avg `5.3392` n `8`; equity avg `3.0544` n `140`; fx avg `-0.0607` n `6`; index avg `0.6508` n `26`; metal avg `0.05` n `20`; unknown avg `4.1527` n `747`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.183`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
