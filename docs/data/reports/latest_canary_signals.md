# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T08:37:24.753256+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0337` n `13`; crypto_alt avg `-0.3086` n `239`; crypto_major avg `-0.4263` n `8`; equity avg `-0.5926` n `166`; fx avg `0.0135` n `6`; index avg `-0.0694` n `27`; metal avg `-0.0785` n `20`; unknown avg `265.2605` n `1266`
- 1h: commodity avg `-0.0344` n `13`; crypto_alt avg `-0.4062` n `239`; crypto_major avg `-0.3708` n `8`; equity avg `-0.5887` n `166`; fx avg `0.0261` n `6`; index avg `-0.0719` n `27`; metal avg `-0.1277` n `20`; unknown avg `0.938` n `1236`
- 4h: commodity avg `0.1441` n `13`; crypto_alt avg `-0.3474` n `239`; crypto_major avg `-0.8046` n `8`; equity avg `-0.9043` n `166`; fx avg `0.0497` n `6`; index avg `-0.1105` n `27`; metal avg `-0.1773` n `20`; unknown avg `0.1463` n `1198`
- 24h: commodity avg `-0.6858` n `13`; crypto_alt avg `-0.0107` n `239`; crypto_major avg `-0.6005` n `8`; equity avg `3.1826` n `166`; fx avg `-0.2377` n `6`; index avg `0.5487` n `27`; metal avg `-0.2463` n `20`; unknown avg `640.2842` n `1112`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
