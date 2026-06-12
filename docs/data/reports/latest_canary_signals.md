# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T03:07:24.335513+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.106` n `12`; crypto_alt avg `0.0368` n `228`; crypto_major avg `-0.0596` n `8`; equity avg `-0.0204` n `74`; fx avg `0.0131` n `6`; index avg `-0.0807` n `23`; metal avg `0.0659` n `18`; unknown avg `-0.0805` n `557`
- 1h: commodity avg `0.233` n `12`; crypto_alt avg `0.1543` n `228`; crypto_major avg `0.3996` n `8`; equity avg `0.0962` n `74`; fx avg `0.013` n `6`; index avg `-0.1277` n `23`; metal avg `0.0777` n `18`; unknown avg `-0.1621` n `557`
- 4h: commodity avg `0.5245` n `12`; crypto_alt avg `0.451` n `228`; crypto_major avg `0.3583` n `8`; equity avg `0.2688` n `74`; fx avg `0.0043` n `6`; index avg `-0.1415` n `23`; metal avg `-0.1668` n `18`; unknown avg `-0.1131` n `556`
- 24h: commodity avg `-2.2109` n `12`; crypto_alt avg `3.3031` n `228`; crypto_major avg `3.27` n `8`; equity avg `4.3035` n `74`; fx avg `0.0203` n `6`; index avg `2.0911` n `23`; metal avg `3.4923` n `18`; unknown avg `2.2668` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
