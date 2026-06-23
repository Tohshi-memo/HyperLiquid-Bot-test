# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T17:52:33.967248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `-0.1549` n `228`; crypto_major avg `-0.1127` n `8`; equity avg `-0.1938` n `86`; fx avg `0.0005` n `6`; index avg `-0.0182` n `23`; metal avg `-0.0072` n `20`; unknown avg `-0.0285` n `764`
- 1h: commodity avg `0.0682` n `12`; crypto_alt avg `-0.2825` n `228`; crypto_major avg `-0.0912` n `8`; equity avg `-0.2279` n `86`; fx avg `-0.0103` n `6`; index avg `-0.0403` n `23`; metal avg `-0.0785` n `20`; unknown avg `-0.4848` n `764`
- 4h: commodity avg `-0.1312` n `12`; crypto_alt avg `-0.8871` n `228`; crypto_major avg `-0.4948` n `8`; equity avg `-0.3488` n `86`; fx avg `-0.0573` n `6`; index avg `-0.055` n `23`; metal avg `-0.1434` n `20`; unknown avg `-0.7475` n `764`
- 24h: commodity avg `-0.3884` n `12`; crypto_alt avg `-3.8872` n `228`; crypto_major avg `-4.1673` n `8`; equity avg `-3.1659` n `86`; fx avg `-0.1722` n `6`; index avg `-0.9282` n `23`; metal avg `-0.9562` n `20`; unknown avg `-0.443` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
