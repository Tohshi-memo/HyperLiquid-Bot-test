# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T12:37:37.597670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0334` n `12`; crypto_alt avg `0.0171` n `228`; crypto_major avg `0.0002` n `8`; equity avg `-0.1223` n `86`; fx avg `0.0022` n `6`; index avg `-0.0204` n `23`; metal avg `0.0379` n `20`; unknown avg `-0.0326` n `764`
- 1h: commodity avg `-0.1258` n `12`; crypto_alt avg `-0.1201` n `228`; crypto_major avg `-0.1197` n `8`; equity avg `-0.2418` n `86`; fx avg `-0.0285` n `6`; index avg `-0.0424` n `23`; metal avg `-0.0367` n `20`; unknown avg `-0.0936` n `764`
- 4h: commodity avg `-0.1957` n `12`; crypto_alt avg `0.7453` n `228`; crypto_major avg `0.2116` n `8`; equity avg `0.322` n `86`; fx avg `-0.0606` n `6`; index avg `-0.0451` n `23`; metal avg `0.0572` n `20`; unknown avg `-0.1256` n `764`
- 24h: commodity avg `-0.4581` n `12`; crypto_alt avg `-4.5189` n `228`; crypto_major avg `-4.7507` n `8`; equity avg `-4.7104` n `85`; fx avg `-0.1972` n `6`; index avg `-0.9964` n `23`; metal avg `-1.3458` n `20`; unknown avg `0.0841` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
