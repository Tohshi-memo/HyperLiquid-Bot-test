# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T14:22:23.864263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2456` n `12`; crypto_alt avg `-0.3625` n `228`; crypto_major avg `-0.2671` n `8`; equity avg `-0.3677` n `66`; fx avg `0.0126` n `5`; index avg `-0.0584` n `23`; metal avg `-0.1344` n `18`; unknown avg `-0.537` n `384`
- 1h: commodity avg `0.55` n `12`; crypto_alt avg `-0.623` n `228`; crypto_major avg `-0.8746` n `8`; equity avg `-1.2522` n `66`; fx avg `0.0132` n `5`; index avg `-0.4967` n `23`; metal avg `-0.3196` n `18`; unknown avg `0.2284` n `383`
- 4h: commodity avg `-0.5141` n `12`; crypto_alt avg `0.6223` n `228`; crypto_major avg `0.2021` n `8`; equity avg `-0.4522` n `66`; fx avg `-0.0233` n `5`; index avg `0.0103` n `23`; metal avg `0.5952` n `18`; unknown avg `0.3925` n `383`
- 24h: commodity avg `0.5048` n `12`; crypto_alt avg `-2.0528` n `228`; crypto_major avg `-1.2759` n `8`; equity avg `-0.3091` n `65`; fx avg `0.0783` n `5`; index avg `0.0687` n `23`; metal avg `0.5248` n `18`; unknown avg `-0.063` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
