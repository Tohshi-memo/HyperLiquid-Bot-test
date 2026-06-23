# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T19:22:26.862614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `-0.1606` n `228`; crypto_major avg `-0.185` n `8`; equity avg `-0.1309` n `86`; fx avg `0.0075` n `6`; index avg `-0.0366` n `23`; metal avg `-0.0379` n `20`; unknown avg `-0.1829` n `756`
- 1h: commodity avg `0.0661` n `12`; crypto_alt avg `0.0225` n `228`; crypto_major avg `-0.2167` n `8`; equity avg `-0.3904` n `86`; fx avg `0.0103` n `6`; index avg `-0.0241` n `23`; metal avg `-0.0597` n `20`; unknown avg `-0.1943` n `756`
- 4h: commodity avg `-0.0736` n `12`; crypto_alt avg `-0.0505` n `228`; crypto_major avg `-0.0134` n `8`; equity avg `-0.4663` n `86`; fx avg `-0.0139` n `6`; index avg `-0.0968` n `23`; metal avg `-0.1147` n `20`; unknown avg `-0.443` n `756`
- 24h: commodity avg `-0.4232` n `12`; crypto_alt avg `-3.2477` n `228`; crypto_major avg `-4.0973` n `8`; equity avg `-3.3428` n `86`; fx avg `-0.1747` n `6`; index avg `-0.9278` n `23`; metal avg `-1.1796` n `20`; unknown avg `-0.2039` n `596`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
