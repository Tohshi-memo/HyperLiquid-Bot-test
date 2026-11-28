# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T07:22:23.283383+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0043` n `13`; crypto_alt avg `0.1874` n `239`; crypto_major avg `0.0321` n `8`; equity avg `0.1188` n `168`; fx avg `-0.0161` n `6`; index avg `0.0109` n `27`; metal avg `0.0181` n `20`; unknown avg `0.0534` n `1267`
- 1h: commodity avg `0.0035` n `13`; crypto_alt avg `0.1684` n `239`; crypto_major avg `-0.1954` n `8`; equity avg `0.1502` n `168`; fx avg `-0.0119` n `6`; index avg `0.001` n `27`; metal avg `0.0446` n `20`; unknown avg `268.2071` n `1253`
- 4h: commodity avg `-0.0257` n `13`; crypto_alt avg `-1.2473` n `239`; crypto_major avg `-0.7307` n `8`; equity avg `-0.1546` n `168`; fx avg `-0.0005` n `6`; index avg `-0.0349` n `27`; metal avg `-0.0147` n `20`; unknown avg `0.4384` n `1209`
- 24h: commodity avg `-0.7845` n `13`; crypto_alt avg `-3.0762` n `239`; crypto_major avg `-2.962` n `8`; equity avg `-0.0748` n `168`; fx avg `-0.121` n `6`; index avg `0.0402` n `27`; metal avg `-0.2377` n `20`; unknown avg `215.2127` n `969`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
