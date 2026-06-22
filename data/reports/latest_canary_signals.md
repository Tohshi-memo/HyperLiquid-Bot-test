# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T15:07:40.130080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0285` n `12`; crypto_alt avg `-0.1953` n `228`; crypto_major avg `-0.2443` n `8`; equity avg `0.1075` n `79`; fx avg `0.0224` n `6`; index avg `-0.0041` n `23`; metal avg `-0.0424` n `20`; unknown avg `0.0558` n `722`
- 1h: commodity avg `0.05` n `12`; crypto_alt avg `-0.581` n `228`; crypto_major avg `-0.747` n `8`; equity avg `-1.1363` n `79`; fx avg `-0.0448` n `6`; index avg `-0.1126` n `23`; metal avg `-0.1869` n `20`; unknown avg `0.2776` n `722`
- 4h: commodity avg `-0.2723` n `12`; crypto_alt avg `0.2171` n `228`; crypto_major avg `0.1267` n `8`; equity avg `-0.3597` n `79`; fx avg `-0.0467` n `6`; index avg `0.0105` n `23`; metal avg `-0.2449` n `20`; unknown avg `0.4513` n `722`
- 24h: commodity avg `-0.711` n `12`; crypto_alt avg `0.0139` n `228`; crypto_major avg `0.2242` n `8`; equity avg `-0.2642` n `79`; fx avg `-0.0532` n `6`; index avg `0.123` n `23`; metal avg `0.3536` n `18`; unknown avg `0.7727` n `637`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
