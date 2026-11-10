# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T18:55:22.084378+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `13`; crypto_alt avg `-0.0966` n `239`; crypto_major avg `0.0219` n `8`; equity avg `0.1068` n `160`; fx avg `0.0123` n `6`; index avg `0.0141` n `27`; metal avg `-0.0066` n `20`; unknown avg `0.6438` n `1260`
- 1h: commodity avg `-0.0471` n `13`; crypto_alt avg `0.5636` n `239`; crypto_major avg `0.7187` n `8`; equity avg `0.3567` n `160`; fx avg `0.0225` n `6`; index avg `0.0439` n `27`; metal avg `0.0568` n `20`; unknown avg `0.0267` n `1254`
- 4h: commodity avg `0.3808` n `13`; crypto_alt avg `-1.3343` n `239`; crypto_major avg `-0.9842` n `8`; equity avg `-1.0465` n `160`; fx avg `-0.0627` n `6`; index avg `-0.11` n `27`; metal avg `-0.0391` n `20`; unknown avg `-0.8321` n `1248`
- 24h: commodity avg `-0.3261` n `13`; crypto_alt avg `-1.4098` n `239`; crypto_major avg `-2.5327` n `8`; equity avg `-1.8253` n `160`; fx avg `-0.0952` n `6`; index avg `-0.1974` n `27`; metal avg `-0.4759` n `20`; unknown avg `0.3467` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2457`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.176`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
