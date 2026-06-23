# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T18:52:37.202694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0483` n `12`; crypto_alt avg `-0.027` n `228`; crypto_major avg `-0.011` n `8`; equity avg `-0.3129` n `86`; fx avg `0.0073` n `6`; index avg `-0.0507` n `23`; metal avg `-0.0927` n `20`; unknown avg `-0.0886` n `764`
- 1h: commodity avg `0.0592` n `12`; crypto_alt avg `0.1651` n `228`; crypto_major avg `-0.1174` n `8`; equity avg `-0.6703` n `86`; fx avg `0.002` n `6`; index avg `-0.1116` n `23`; metal avg `-0.2025` n `20`; unknown avg `-0.2746` n `764`
- 4h: commodity avg `-0.0251` n `12`; crypto_alt avg `-0.5861` n `228`; crypto_major avg `-0.535` n `8`; equity avg `-1.0147` n `86`; fx avg `-0.0181` n `6`; index avg `-0.1667` n `23`; metal avg `-0.2122` n `20`; unknown avg `-0.8155` n `764`
- 24h: commodity avg `-0.3544` n `12`; crypto_alt avg `-3.4359` n `228`; crypto_major avg `-4.2753` n `8`; equity avg `-3.6591` n `86`; fx avg `-0.1634` n `6`; index avg `-0.9579` n `23`; metal avg `-1.2549` n `20`; unknown avg `-0.4174` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
