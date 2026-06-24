# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T11:52:31.775606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0591` n `12`; crypto_alt avg `0.6864` n `228`; crypto_major avg `0.6495` n `8`; equity avg `0.1439` n `86`; fx avg `-0.0117` n `6`; index avg `0.0354` n `23`; metal avg `0.0419` n `20`; unknown avg `0.1071` n `764`
- 1h: commodity avg `-0.0663` n `12`; crypto_alt avg `0.6409` n `228`; crypto_major avg `0.7665` n `8`; equity avg `0.1557` n `86`; fx avg `-0.0113` n `6`; index avg `0.0199` n `23`; metal avg `-0.1895` n `20`; unknown avg `0.2635` n `764`
- 4h: commodity avg `-0.1357` n `12`; crypto_alt avg `0.3713` n `228`; crypto_major avg `0.4362` n `8`; equity avg `0.157` n `86`; fx avg `-0.0482` n `6`; index avg `0.0726` n `23`; metal avg `-0.5927` n `20`; unknown avg `-0.059` n `764`
- 24h: commodity avg `-0.5127` n `12`; crypto_alt avg `0.1481` n `228`; crypto_major avg `0.2656` n `8`; equity avg `4.4614` n `86`; fx avg `-0.0418` n `6`; index avg `0.1193` n `23`; metal avg `-0.8364` n `20`; unknown avg `0.082` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
