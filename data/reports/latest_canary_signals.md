# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T03:22:29.004202+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0474` n `13`; crypto_alt avg `-0.0091` n `239`; crypto_major avg `-0.0408` n `8`; equity avg `-0.1339` n `160`; fx avg `-0.0092` n `6`; index avg `-0.0119` n `27`; metal avg `-0.0049` n `20`; unknown avg `2.6355` n `1259`
- 1h: commodity avg `-0.1142` n `13`; crypto_alt avg `0.1459` n `239`; crypto_major avg `-0.0064` n `8`; equity avg `-0.2708` n `160`; fx avg `-0.0083` n `6`; index avg `-0.0523` n `27`; metal avg `-0.0609` n `20`; unknown avg `0.2241` n `1253`
- 4h: commodity avg `-0.143` n `13`; crypto_alt avg `-0.2024` n `239`; crypto_major avg `-0.4372` n `8`; equity avg `-0.3731` n `160`; fx avg `0.0346` n `6`; index avg `-0.1331` n `27`; metal avg `-0.1458` n `20`; unknown avg `-0.0698` n `1245`
- 24h: commodity avg `-0.7862` n `13`; crypto_alt avg `0.6544` n `239`; crypto_major avg `-0.3708` n `8`; equity avg `3.389` n `160`; fx avg `0.0244` n `6`; index avg `0.3406` n `27`; metal avg `0.0683` n `20`; unknown avg `183.8885` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
