# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T02:22:26.303770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0182` n `12`; crypto_alt avg `-0.2005` n `230`; crypto_major avg `-0.1104` n `8`; equity avg `-0.2809` n `121`; fx avg `-0.0197` n `6`; index avg `-0.054` n `25`; metal avg `-0.0456` n `20`; unknown avg `-0.0135` n `792`
- 1h: commodity avg `-0.02` n `12`; crypto_alt avg `0.1291` n `230`; crypto_major avg `0.2922` n `8`; equity avg `-0.1327` n `121`; fx avg `0.0145` n `6`; index avg `0.015` n `25`; metal avg `-0.0307` n `20`; unknown avg `0.0205` n `792`
- 4h: commodity avg `0.0793` n `12`; crypto_alt avg `0.0702` n `230`; crypto_major avg `-0.777` n `8`; equity avg `0.1404` n `121`; fx avg `0.1141` n `6`; index avg `0.0841` n `25`; metal avg `-0.199` n `20`; unknown avg `-0.1244` n `792`
- 24h: commodity avg `-0.0885` n `12`; crypto_alt avg `5.6114` n `230`; crypto_major avg `9.9644` n `8`; equity avg `0.7261` n `120`; fx avg `0.0041` n `6`; index avg `0.2653` n `25`; metal avg `0.9551` n `20`; unknown avg `1.5856` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
