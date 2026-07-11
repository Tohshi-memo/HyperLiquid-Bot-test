# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T11:22:26.262884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `-0.0145` n `230`; crypto_major avg `-0.0554` n `8`; equity avg `-0.0163` n `92`; fx avg `0.0075` n `6`; index avg `-0.0003` n `25`; metal avg `0.0024` n `20`; unknown avg `-0.0352` n `765`
- 1h: commodity avg `-0.0136` n `12`; crypto_alt avg `0.004` n `230`; crypto_major avg `0.1277` n `8`; equity avg `0.0194` n `92`; fx avg `0.008` n `6`; index avg `0.0006` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.1246` n `765`
- 4h: commodity avg `0.0098` n `12`; crypto_alt avg `0.1169` n `230`; crypto_major avg `0.1212` n `8`; equity avg `-0.0031` n `92`; fx avg `0.006` n `6`; index avg `-0.0003` n `25`; metal avg `-0.0024` n `20`; unknown avg `-0.1288` n `761`
- 24h: commodity avg `-0.2914` n `12`; crypto_alt avg `-0.0341` n `229`; crypto_major avg `-0.6487` n `8`; equity avg `-0.5813` n `92`; fx avg `-0.088` n `6`; index avg `0.0878` n `25`; metal avg `0.1343` n `20`; unknown avg `2.7463` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
