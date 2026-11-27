# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T10:07:23.662365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0493` n `13`; crypto_alt avg `-0.0154` n `239`; crypto_major avg `-0.1297` n `8`; equity avg `-0.2851` n `168`; fx avg `-0.0089` n `6`; index avg `-0.0143` n `27`; metal avg `-0.0986` n `20`; unknown avg `0.8298` n `1249`
- 1h: commodity avg `-0.0458` n `13`; crypto_alt avg `-0.0354` n `239`; crypto_major avg `-0.0281` n `8`; equity avg `-0.562` n `168`; fx avg `0.0004` n `6`; index avg `-0.0801` n `27`; metal avg `-0.1511` n `20`; unknown avg `0.7321` n `1253`
- 4h: commodity avg `-0.2819` n `13`; crypto_alt avg `-0.0285` n `239`; crypto_major avg `0.0485` n `8`; equity avg `-0.2694` n `168`; fx avg `-0.0869` n `6`; index avg `-0.0566` n `27`; metal avg `0.1442` n `20`; unknown avg `5.0475` n `1113`
- 24h: commodity avg `0.2843` n `13`; crypto_alt avg `1.9922` n `239`; crypto_major avg `2.602` n `8`; equity avg `3.6504` n `168`; fx avg `-0.0927` n `6`; index avg `0.2697` n `27`; metal avg `1.124` n `20`; unknown avg `43.9816` n `1021`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
