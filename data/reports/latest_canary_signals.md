# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T14:07:29.028371+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0549` n `13`; crypto_alt avg `0.1746` n `239`; crypto_major avg `-0.0392` n `8`; equity avg `0.1813` n `160`; fx avg `0.0113` n `6`; index avg `0.0066` n `27`; metal avg `-0.0472` n `20`; unknown avg `0.2255` n `1260`
- 1h: commodity avg `-0.1162` n `13`; crypto_alt avg `0.0248` n `239`; crypto_major avg `-0.552` n `8`; equity avg `-0.769` n `160`; fx avg `0.0022` n `6`; index avg `-0.0757` n `27`; metal avg `-0.1237` n `20`; unknown avg `18.521` n `1256`
- 4h: commodity avg `-0.0314` n `13`; crypto_alt avg `0.0295` n `239`; crypto_major avg `-0.8953` n `8`; equity avg `-1.8999` n `160`; fx avg `0.0027` n `6`; index avg `-0.1389` n `27`; metal avg `-0.1996` n `20`; unknown avg `20.3806` n `1250`
- 24h: commodity avg `-0.6346` n `13`; crypto_alt avg `-0.3705` n `239`; crypto_major avg `-1.0907` n `8`; equity avg `1.7377` n `160`; fx avg `-0.0342` n `6`; index avg `0.2443` n `27`; metal avg `-0.2541` n `20`; unknown avg `0.9871` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
