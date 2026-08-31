# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T19:37:26.203506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0379` n `12`; crypto_alt avg `-0.1205` n `232`; crypto_major avg `-0.0628` n `8`; equity avg `0.0901` n `129`; fx avg `-0.0003` n `6`; index avg `0.0152` n `26`; metal avg `0.0511` n `20`; unknown avg `0.6038` n `793`
- 1h: commodity avg `-0.0555` n `12`; crypto_alt avg `-0.3086` n `232`; crypto_major avg `-0.1999` n `8`; equity avg `0.1542` n `129`; fx avg `-0.0025` n `6`; index avg `0.0187` n `26`; metal avg `0.1113` n `20`; unknown avg `0.3117` n `791`
- 4h: commodity avg `0.041` n `12`; crypto_alt avg `0.521` n `232`; crypto_major avg `0.7075` n `8`; equity avg `0.1858` n `129`; fx avg `-0.0276` n `6`; index avg `0.0033` n `26`; metal avg `0.0671` n `20`; unknown avg `-0.2281` n `791`
- 24h: commodity avg `0.4096` n `12`; crypto_alt avg `-1.0444` n `231`; crypto_major avg `-0.9221` n `8`; equity avg `-0.3841` n `129`; fx avg `-0.0919` n `6`; index avg `-0.2096` n `26`; metal avg `-0.493` n `20`; unknown avg `0.3434` n `758`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
