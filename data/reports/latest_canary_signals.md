# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T09:37:30.822108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.18` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0084` n `13`; crypto_alt avg `-0.2431` n `239`; crypto_major avg `-0.1013` n `8`; equity avg `-0.0031` n `168`; fx avg `-0.002` n `6`; index avg `0.0021` n `27`; metal avg `0.0035` n `20`; unknown avg `93.4552` n `1265`
- 1h: commodity avg `-0.0269` n `13`; crypto_alt avg `-0.1052` n `239`; crypto_major avg `-0.0954` n `8`; equity avg `-0.0341` n `168`; fx avg `0.0041` n `6`; index avg `-0.0065` n `27`; metal avg `-0.0054` n `20`; unknown avg `-0.1338` n `1229`
- 4h: commodity avg `-0.0445` n `13`; crypto_alt avg `-0.2867` n `239`; crypto_major avg `-0.376` n `8`; equity avg `-0.025` n `168`; fx avg `0.0031` n `6`; index avg `-0.0219` n `27`; metal avg `0.0178` n `20`; unknown avg `0.1702` n `1191`
- 24h: commodity avg `-0.6661` n `13`; crypto_alt avg `-3.4773` n `239`; crypto_major avg `-3.3339` n `8`; equity avg `-0.714` n `168`; fx avg `-0.065` n `6`; index avg `0.0104` n `27`; metal avg `-0.3868` n `20`; unknown avg `190.6038` n `1087`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
