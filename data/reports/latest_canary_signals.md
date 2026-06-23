# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T14:07:35.519780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1519` n `12`; crypto_alt avg `-0.0641` n `228`; crypto_major avg `-0.0291` n `8`; equity avg `0.3744` n `86`; fx avg `-0.0018` n `6`; index avg `0.0531` n `23`; metal avg `-0.0527` n `20`; unknown avg `0.0921` n `764`
- 1h: commodity avg `-0.2492` n `12`; crypto_alt avg `0.7401` n `228`; crypto_major avg `0.385` n `8`; equity avg `1.7619` n `86`; fx avg `-0.0192` n `6`; index avg `0.1988` n `23`; metal avg `0.137` n `20`; unknown avg `0.332` n `764`
- 4h: commodity avg `-0.2532` n `12`; crypto_alt avg `0.53` n `228`; crypto_major avg `0.1662` n `8`; equity avg `1.2222` n `86`; fx avg `-0.0466` n `6`; index avg `0.0444` n `23`; metal avg `-0.0591` n `20`; unknown avg `0.0991` n `764`
- 24h: commodity avg `-0.4804` n `12`; crypto_alt avg `-4.2563` n `228`; crypto_major avg `-4.8953` n `8`; equity avg `-3.7749` n `85`; fx avg `-0.1656` n `6`; index avg `-0.9376` n `23`; metal avg `-1.2527` n `20`; unknown avg `-0.3504` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
