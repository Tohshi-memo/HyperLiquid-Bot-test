# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T15:14:54.044421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0736` n `12`; crypto_alt avg `0.0724` n `228`; crypto_major avg `-0.0388` n `8`; equity avg `-0.2632` n `86`; fx avg `-0.0391` n `6`; index avg `-0.0535` n `23`; metal avg `-0.1167` n `20`; unknown avg `-0.0159` n `765`
- 1h: commodity avg `-0.0824` n `12`; crypto_alt avg `0.1724` n `228`; crypto_major avg `0.0663` n `8`; equity avg `-0.335` n `86`; fx avg `-0.0538` n `6`; index avg `-0.0675` n `23`; metal avg `-0.026` n `20`; unknown avg `-0.0144` n `765`
- 4h: commodity avg `-0.2255` n `12`; crypto_alt avg `0.8701` n `228`; crypto_major avg `0.9189` n `8`; equity avg `0.6108` n `86`; fx avg `-0.0415` n `6`; index avg `0.0508` n `23`; metal avg `0.2153` n `20`; unknown avg `0.0781` n `765`
- 24h: commodity avg `-0.4313` n `12`; crypto_alt avg `1.3289` n `228`; crypto_major avg `2.2018` n `8`; equity avg `-1.0471` n `86`; fx avg `-0.035` n `6`; index avg `-0.312` n `23`; metal avg `0.6284` n `20`; unknown avg `0.0966` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.3898`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2639`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.2309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2301`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
