# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T17:37:35.321301+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0237` n `12`; crypto_alt avg `0.1194` n `228`; crypto_major avg `0.1832` n `8`; equity avg `0.0362` n `86`; fx avg `-0.007` n `6`; index avg `-0.0053` n `23`; metal avg `-0.0684` n `20`; unknown avg `0.2382` n `764`
- 1h: commodity avg `0.0345` n `12`; crypto_alt avg `-0.0341` n `228`; crypto_major avg `0.1126` n `8`; equity avg `-0.0201` n `86`; fx avg `-0.0021` n `6`; index avg `-0.0242` n `23`; metal avg `-0.0873` n `20`; unknown avg `-0.371` n `764`
- 4h: commodity avg `-0.0476` n `12`; crypto_alt avg `-0.1948` n `228`; crypto_major avg `0.0283` n `8`; equity avg `0.9441` n `86`; fx avg `-0.06` n `6`; index avg `0.1156` n `23`; metal avg `0.0289` n `20`; unknown avg `-0.5112` n `764`
- 24h: commodity avg `-0.4824` n `12`; crypto_alt avg `-3.3227` n `228`; crypto_major avg `-3.5669` n `8`; equity avg `-2.7245` n `86`; fx avg `-0.1801` n `6`; index avg `-0.8954` n `23`; metal avg `-0.8915` n `20`; unknown avg `-0.0757` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
