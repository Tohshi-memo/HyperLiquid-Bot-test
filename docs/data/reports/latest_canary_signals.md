# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T19:37:38.418445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0377` n `12`; crypto_alt avg `-0.1651` n `232`; crypto_major avg `0.0619` n `8`; equity avg `0.0458` n `133`; fx avg `0.0055` n `6`; index avg `0.0052` n `26`; metal avg `0.0043` n `20`; unknown avg `28.8249` n `792`
- 1h: commodity avg `-0.0098` n `12`; crypto_alt avg `0.1355` n `232`; crypto_major avg `0.6207` n `8`; equity avg `-0.0289` n `133`; fx avg `0.0019` n `6`; index avg `-0.024` n `26`; metal avg `-0.0268` n `20`; unknown avg `0.0354` n `790`
- 4h: commodity avg `-0.0417` n `12`; crypto_alt avg `0.8398` n `232`; crypto_major avg `1.0859` n `8`; equity avg `0.3001` n `133`; fx avg `0.036` n `6`; index avg `0.0353` n `26`; metal avg `-0.1131` n `20`; unknown avg `30.4436` n `790`
- 24h: commodity avg `-0.189` n `12`; crypto_alt avg `4.9765` n `232`; crypto_major avg `6.0253` n `8`; equity avg `1.489` n `133`; fx avg `-0.2552` n `6`; index avg `0.1771` n `26`; metal avg `0.8112` n `20`; unknown avg `0.9825` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
