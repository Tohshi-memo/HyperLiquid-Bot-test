# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T22:37:29.720511+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0116` n `12`; crypto_alt avg `0.0498` n `232`; crypto_major avg `-0.0325` n `8`; equity avg `-0.001` n `129`; fx avg `0.0123` n `6`; index avg `-0.0028` n `26`; metal avg `0.0021` n `20`; unknown avg `1.3314` n `793`
- 1h: commodity avg `-0.0065` n `12`; crypto_alt avg `-0.164` n `232`; crypto_major avg `-0.3397` n `8`; equity avg `0.0216` n `129`; fx avg `0.0093` n `6`; index avg `-0.0106` n `26`; metal avg `-0.0071` n `20`; unknown avg `0.6788` n `791`
- 4h: commodity avg `0.0182` n `12`; crypto_alt avg `-0.1575` n `232`; crypto_major avg `-0.383` n `8`; equity avg `0.5159` n `129`; fx avg `0.0116` n `6`; index avg `0.0649` n `26`; metal avg `0.1289` n `20`; unknown avg `0.8096` n `773`
- 24h: commodity avg `0.365` n `12`; crypto_alt avg `0.272` n `231`; crypto_major avg `0.4489` n `8`; equity avg `0.3809` n `129`; fx avg `-0.0799` n `6`; index avg `-0.0604` n `26`; metal avg `-0.2853` n `20`; unknown avg `-0.1108` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
