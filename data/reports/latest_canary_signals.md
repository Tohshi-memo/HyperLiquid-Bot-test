# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T02:22:29.904999+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0368` n `13`; crypto_alt avg `-0.2219` n `239`; crypto_major avg `-0.1396` n `8`; equity avg `0.1425` n `160`; fx avg `-0.0011` n `6`; index avg `0.0073` n `27`; metal avg `0.0167` n `20`; unknown avg `0.0069` n `1261`
- 1h: commodity avg `-0.0515` n `13`; crypto_alt avg `-0.3394` n `239`; crypto_major avg `-0.4451` n `8`; equity avg `0.274` n `160`; fx avg `0.0194` n `6`; index avg `0.036` n `27`; metal avg `-0.0644` n `20`; unknown avg `0.0631` n `1255`
- 4h: commodity avg `-0.1609` n `13`; crypto_alt avg `-0.5845` n `239`; crypto_major avg `-0.2749` n `8`; equity avg `-0.1389` n `160`; fx avg `0.0787` n `6`; index avg `-0.0795` n `27`; metal avg `-0.0465` n `20`; unknown avg `0.0447` n `1249`
- 24h: commodity avg `-0.5121` n `13`; crypto_alt avg `0.1228` n `239`; crypto_major avg `-1.0028` n `8`; equity avg `3.4237` n `160`; fx avg `0.0294` n `6`; index avg `0.3598` n `27`; metal avg `0.0758` n `20`; unknown avg `184.0591` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
