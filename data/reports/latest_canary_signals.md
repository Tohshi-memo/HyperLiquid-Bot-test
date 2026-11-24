# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T05:22:29.015137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0529` n `13`; crypto_alt avg `0.3628` n `239`; crypto_major avg `0.2312` n `8`; equity avg `-0.208` n `166`; fx avg `0.0225` n `6`; index avg `-0.0133` n `27`; metal avg `-0.0413` n `20`; unknown avg `-0.1572` n `1262`
- 1h: commodity avg `-0.1212` n `13`; crypto_alt avg `0.5426` n `239`; crypto_major avg `0.2562` n `8`; equity avg `0.0421` n `166`; fx avg `0.0083` n `6`; index avg `0.0039` n `27`; metal avg `-0.0089` n `20`; unknown avg `1.0113` n `1256`
- 4h: commodity avg `-0.1874` n `13`; crypto_alt avg `0.0252` n `239`; crypto_major avg `-0.694` n `8`; equity avg `-1.2183` n `166`; fx avg `-0.0326` n `6`; index avg `-0.0716` n `27`; metal avg `-0.4807` n `20`; unknown avg `161.7611` n `1240`
- 24h: commodity avg `-1.3587` n `13`; crypto_alt avg `0.9296` n `239`; crypto_major avg `0.3168` n `8`; equity avg `4.6127` n `166`; fx avg `-0.2546` n `6`; index avg `0.6476` n `27`; metal avg `-0.0565` n `20`; unknown avg `292.0057` n `1032`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
