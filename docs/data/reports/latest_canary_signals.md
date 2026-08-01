# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T01:22:56.585636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0767` n `12`; crypto_alt avg `-0.0382` n `230`; crypto_major avg `0.0123` n `8`; equity avg `-0.0288` n `102`; fx avg `-0.0018` n `6`; index avg `0.0052` n `25`; metal avg `0.0011` n `20`; unknown avg `-0.1038` n `781`
- 1h: commodity avg `-0.1554` n `12`; crypto_alt avg `0.2465` n `230`; crypto_major avg `0.1949` n `8`; equity avg `-0.0133` n `102`; fx avg `0.003` n `6`; index avg `-0.0152` n `25`; metal avg `0.0008` n `20`; unknown avg `-0.1694` n `781`
- 4h: commodity avg `-0.0567` n `12`; crypto_alt avg `0.4412` n `230`; crypto_major avg `0.0586` n `8`; equity avg `-0.1053` n `102`; fx avg `-0.0102` n `6`; index avg `-0.0486` n `25`; metal avg `-0.0088` n `20`; unknown avg `2.0581` n `781`
- 24h: commodity avg `0.8266` n `12`; crypto_alt avg `-0.5847` n `230`; crypto_major avg `-2.3133` n `8`; equity avg `-2.8878` n `102`; fx avg `-0.1299` n `6`; index avg `-0.4104` n `25`; metal avg `-0.2507` n `20`; unknown avg `2.6313` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
