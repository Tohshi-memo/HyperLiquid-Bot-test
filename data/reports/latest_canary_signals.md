# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T10:52:32.249380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0312` n `12`; crypto_alt avg `0.0329` n `230`; crypto_major avg `0.0336` n `8`; equity avg `0.0853` n `92`; fx avg `0.013` n `6`; index avg `0.0149` n `25`; metal avg `0.0185` n `20`; unknown avg `-0.0154` n `766`
- 1h: commodity avg `0.2145` n `12`; crypto_alt avg `0.1158` n `230`; crypto_major avg `-0.1753` n `8`; equity avg `-0.0609` n `92`; fx avg `0.0026` n `6`; index avg `-0.0372` n `25`; metal avg `-0.0866` n `20`; unknown avg `-0.005` n `766`
- 4h: commodity avg `-0.0553` n `12`; crypto_alt avg `0.2805` n `230`; crypto_major avg `-0.0171` n `8`; equity avg `0.531` n `92`; fx avg `-0.0639` n `6`; index avg `0.0781` n `25`; metal avg `0.1448` n `20`; unknown avg `-0.0654` n `766`
- 24h: commodity avg `-0.1183` n `12`; crypto_alt avg `-0.9438` n `230`; crypto_major avg `-1.1319` n `8`; equity avg `-1.9511` n `92`; fx avg `-0.0562` n `6`; index avg `-0.4483` n `25`; metal avg `-0.2631` n `20`; unknown avg `-0.0847` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1921`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1737`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
