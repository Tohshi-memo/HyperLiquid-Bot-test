# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T11:07:24.263296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1158` n `12`; crypto_alt avg `0.0404` n `228`; crypto_major avg `0.1709` n `8`; equity avg `0.0995` n `66`; fx avg `-0.0286` n `6`; index avg `0.0777` n `23`; metal avg `0.2156` n `18`; unknown avg `0.1021` n `383`
- 1h: commodity avg `0.2838` n `12`; crypto_alt avg `-0.2925` n `228`; crypto_major avg `0.1466` n `8`; equity avg `0.0354` n `66`; fx avg `-0.0312` n `6`; index avg `0.0391` n `23`; metal avg `0.1047` n `18`; unknown avg `0.0171` n `383`
- 4h: commodity avg `0.11` n `12`; crypto_alt avg `-0.8395` n `228`; crypto_major avg `-0.2091` n `8`; equity avg `-0.5796` n `66`; fx avg `-0.0496` n `6`; index avg `-0.3555` n `23`; metal avg `-0.1473` n `18`; unknown avg `-0.4659` n `383`
- 24h: commodity avg `0.5961` n `12`; crypto_alt avg `1.4011` n `228`; crypto_major avg `1.0747` n `8`; equity avg `-1.302` n `66`; fx avg `0.2039` n `6`; index avg `-0.6883` n `23`; metal avg `0.1106` n `18`; unknown avg `0.6817` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
