# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T08:07:29.546426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0432` n `12`; crypto_alt avg `0.2098` n `228`; crypto_major avg `0.1935` n `8`; equity avg `0.2442` n `74`; fx avg `-0.0195` n `6`; index avg `0.216` n `23`; metal avg `0.177` n `18`; unknown avg `0.2127` n `556`
- 1h: commodity avg `-0.226` n `12`; crypto_alt avg `0.3084` n `228`; crypto_major avg `0.2602` n `8`; equity avg `0.468` n `74`; fx avg `-0.0363` n `6`; index avg `0.2584` n `23`; metal avg `0.3907` n `18`; unknown avg `0.2348` n `548`
- 4h: commodity avg `-1.0006` n `12`; crypto_alt avg `0.2436` n `228`; crypto_major avg `0.3763` n `8`; equity avg `0.7563` n `74`; fx avg `0.0409` n `6`; index avg `0.3931` n `23`; metal avg `0.7664` n `18`; unknown avg `0.1741` n `530`
- 24h: commodity avg `0.4664` n `12`; crypto_alt avg `1.0983` n `228`; crypto_major avg `1.0889` n `8`; equity avg `0.389` n `74`; fx avg `0.0051` n `6`; index avg `-0.1086` n `23`; metal avg `0.1934` n `18`; unknown avg `3.8418` n `527`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
