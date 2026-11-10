# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T02:52:30.357528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0754` n `13`; crypto_alt avg `0.2193` n `239`; crypto_major avg `0.2753` n `8`; equity avg `0.0034` n `160`; fx avg `-0.0154` n `6`; index avg `0.0061` n `27`; metal avg `-0.0059` n `20`; unknown avg `-0.0313` n `1261`
- 1h: commodity avg `-0.0583` n `13`; crypto_alt avg `-0.0414` n `239`; crypto_major avg `-0.2206` n `8`; equity avg `0.0742` n `160`; fx avg `0.0034` n `6`; index avg `-0.0036` n `27`; metal avg `-0.0485` n `20`; unknown avg `0.5039` n `1255`
- 4h: commodity avg `-0.1821` n `13`; crypto_alt avg `-0.5921` n `239`; crypto_major avg `-0.533` n `8`; equity avg `-0.219` n `160`; fx avg `0.0662` n `6`; index avg `-0.0991` n `27`; metal avg `-0.1202` n `20`; unknown avg `0.1594` n `1247`
- 24h: commodity avg `-0.6721` n `13`; crypto_alt avg `0.2163` n `239`; crypto_major avg `-0.7375` n `8`; equity avg `3.315` n `160`; fx avg `0.0557` n `6`; index avg `0.3452` n `27`; metal avg `0.0315` n `20`; unknown avg `183.7859` n `1070`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
