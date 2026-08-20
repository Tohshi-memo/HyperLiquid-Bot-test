# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T00:52:35.626475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0031` n `12`; crypto_alt avg `-0.1547` n `230`; crypto_major avg `-0.1299` n `8`; equity avg `0.0745` n `121`; fx avg `0.0655` n `6`; index avg `0.0195` n `25`; metal avg `-0.0318` n `20`; unknown avg `0.394` n `792`
- 1h: commodity avg `0.0479` n `12`; crypto_alt avg `0.5452` n `230`; crypto_major avg `0.6352` n `8`; equity avg `0.151` n `121`; fx avg `0.0649` n `6`; index avg `0.0573` n `25`; metal avg `-0.0351` n `20`; unknown avg `0.1043` n `792`
- 4h: commodity avg `0.0621` n `12`; crypto_alt avg `0.6497` n `230`; crypto_major avg `0.9789` n `8`; equity avg `0.6337` n `121`; fx avg `0.0749` n `6`; index avg `0.1312` n `25`; metal avg `-0.0369` n `20`; unknown avg `0.2771` n `792`
- 24h: commodity avg `-0.0882` n `12`; crypto_alt avg `5.7013` n `230`; crypto_major avg `9.9842` n `8`; equity avg `1.2975` n `120`; fx avg `-0.0708` n `6`; index avg `0.2484` n `25`; metal avg `1.1548` n `20`; unknown avg `1.5019` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
