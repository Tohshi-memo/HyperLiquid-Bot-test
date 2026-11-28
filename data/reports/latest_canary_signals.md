# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T16:22:26.780842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.008` n `13`; crypto_alt avg `-0.2182` n `239`; crypto_major avg `-0.1613` n `8`; equity avg `-0.0383` n `168`; fx avg `-0.0093` n `6`; index avg `-0.0024` n `27`; metal avg `-0.0064` n `20`; unknown avg `-0.3019` n `1265`
- 1h: commodity avg `-0.0162` n `13`; crypto_alt avg `-0.6527` n `239`; crypto_major avg `-0.2139` n `8`; equity avg `-0.1183` n `168`; fx avg `0.0011` n `6`; index avg `-0.0045` n `27`; metal avg `-0.0052` n `20`; unknown avg `-0.273` n `1245`
- 4h: commodity avg `-0.0174` n `13`; crypto_alt avg `-1.3307` n `239`; crypto_major avg `-0.28` n `8`; equity avg `-0.2322` n `168`; fx avg `0.0007` n `6`; index avg `-0.0104` n `27`; metal avg `-0.0445` n `20`; unknown avg `2.2388` n `1237`
- 24h: commodity avg `-0.1333` n `13`; crypto_alt avg `-2.9183` n `239`; crypto_major avg `-1.4394` n `8`; equity avg `0.4648` n `168`; fx avg `-0.0241` n `6`; index avg `0.056` n `27`; metal avg `0.3122` n `20`; unknown avg `200.3889` n `1082`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
