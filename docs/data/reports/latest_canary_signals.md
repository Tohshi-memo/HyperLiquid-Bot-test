# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T19:07:32.514859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0476` n `13`; crypto_alt avg `0.1515` n `239`; crypto_major avg `0.0941` n `8`; equity avg `-0.15` n `160`; fx avg `0.0031` n `6`; index avg `-0.0132` n `27`; metal avg `-0.0139` n `20`; unknown avg `19.0301` n `1257`
- 1h: commodity avg `-0.0559` n `13`; crypto_alt avg `0.0203` n `239`; crypto_major avg `-0.1009` n `8`; equity avg `-0.0541` n `160`; fx avg `0.0074` n `6`; index avg `0.0041` n `27`; metal avg `0.0367` n `20`; unknown avg `19.0965` n `1255`
- 4h: commodity avg `0.1315` n `13`; crypto_alt avg `-0.0829` n `239`; crypto_major avg `-0.2327` n `8`; equity avg `1.0236` n `160`; fx avg `-0.0048` n `6`; index avg `0.1118` n `27`; metal avg `0.0332` n `20`; unknown avg `-0.2836` n `1249`
- 24h: commodity avg `-0.116` n `13`; crypto_alt avg `0.4671` n `239`; crypto_major avg `-2.5875` n `8`; equity avg `3.3968` n `160`; fx avg `-0.1335` n `6`; index avg `0.4193` n `27`; metal avg `0.4053` n `20`; unknown avg `5.423` n `1074`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1749`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1512`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1433`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1366`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.133`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1316`, n `669`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1192`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.107`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1012`, n `669`, weak_sample_signal
