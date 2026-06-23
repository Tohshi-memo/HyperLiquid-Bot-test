# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T17:22:34.389345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0245` n `12`; crypto_alt avg `0.2526` n `228`; crypto_major avg `0.2899` n `8`; equity avg `0.2199` n `86`; fx avg `0.0007` n `6`; index avg `0.0294` n `23`; metal avg `0.0485` n `20`; unknown avg `-0.0645` n `764`
- 1h: commodity avg `-0.0451` n `12`; crypto_alt avg `-0.1997` n `228`; crypto_major avg `-0.1601` n `8`; equity avg `-0.0657` n `86`; fx avg `-0.0045` n `6`; index avg `-0.0203` n `23`; metal avg `-0.0405` n `20`; unknown avg `-0.5034` n `764`
- 4h: commodity avg `-0.1416` n `12`; crypto_alt avg `0.1779` n `228`; crypto_major avg `0.1033` n `8`; equity avg `1.2757` n `86`; fx avg `-0.0632` n `6`; index avg `0.1336` n `23`; metal avg `0.2097` n `20`; unknown avg `-0.4332` n `764`
- 24h: commodity avg `-0.4606` n `12`; crypto_alt avg `-3.6207` n `228`; crypto_major avg `-3.8368` n `8`; equity avg `-2.8113` n `86`; fx avg `-0.1727` n `6`; index avg `-0.8922` n `23`; metal avg `-0.953` n `20`; unknown avg `-0.2058` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
