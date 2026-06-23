# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T21:37:30.909140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `0.0591` n `228`; crypto_major avg `0.1236` n `8`; equity avg `0.022` n `86`; fx avg `-0.001` n `6`; index avg `0.0293` n `23`; metal avg `0.012` n `20`; unknown avg `0.1567` n `764`
- 1h: commodity avg `-0.0353` n `12`; crypto_alt avg `0.1244` n `228`; crypto_major avg `0.0842` n `8`; equity avg `-0.0196` n `86`; fx avg `-0.0064` n `6`; index avg `0.0427` n `23`; metal avg `0.0634` n `20`; unknown avg `0.4549` n `764`
- 4h: commodity avg `0.025` n `12`; crypto_alt avg `0.6974` n `228`; crypto_major avg `0.1916` n `8`; equity avg `-0.5149` n `86`; fx avg `0.0047` n `6`; index avg `-0.0335` n `23`; metal avg `-0.1097` n `20`; unknown avg `0.7582` n `756`
- 24h: commodity avg `-0.4133` n `12`; crypto_alt avg `-2.4047` n `228`; crypto_major avg `-3.3916` n `8`; equity avg `-3.2719` n `86`; fx avg `-0.1491` n `6`; index avg `-0.9024` n `23`; metal avg `-1.174` n `20`; unknown avg `1.0445` n `596`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
