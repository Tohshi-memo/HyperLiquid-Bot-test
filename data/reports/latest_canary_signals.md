# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T09:37:37.905452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0462` n `12`; crypto_alt avg `-0.0291` n `228`; crypto_major avg `-0.0687` n `8`; equity avg `-0.0676` n `86`; fx avg `-0.0058` n `6`; index avg `-0.0018` n `23`; metal avg `-0.0464` n `20`; unknown avg `-0.0406` n `764`
- 1h: commodity avg `-0.0034` n `12`; crypto_alt avg `-0.0829` n `228`; crypto_major avg `-0.2116` n `8`; equity avg `-0.0916` n `86`; fx avg `0.0272` n `6`; index avg `-0.0294` n `23`; metal avg `-0.1109` n `20`; unknown avg `-0.1842` n `764`
- 4h: commodity avg `-0.1072` n `12`; crypto_alt avg `-0.4156` n `228`; crypto_major avg `-0.6689` n `8`; equity avg `-0.2162` n `86`; fx avg `0.0353` n `6`; index avg `-0.0157` n `23`; metal avg `-0.1723` n `20`; unknown avg `-0.1337` n `740`
- 24h: commodity avg `-0.4345` n `12`; crypto_alt avg `0.2171` n `228`; crypto_major avg `0.0881` n `8`; equity avg `4.6532` n `86`; fx avg `-0.0012` n `6`; index avg `0.0341` n `23`; metal avg `-0.5471` n `20`; unknown avg `0.0011` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
