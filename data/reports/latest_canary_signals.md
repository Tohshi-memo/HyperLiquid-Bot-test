# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T12:37:35.142158+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2179` n `12`; crypto_alt avg `0.1323` n `228`; crypto_major avg `0.0939` n `8`; equity avg `-0.0514` n `77`; fx avg `0.0076` n `6`; index avg `-0.0301` n `23`; metal avg `0.2492` n `18`; unknown avg `0.0797` n `687`
- 1h: commodity avg `-0.6048` n `12`; crypto_alt avg `0.7374` n `228`; crypto_major avg `0.8558` n `8`; equity avg `-0.3396` n `77`; fx avg `-0.027` n `6`; index avg `-0.1149` n `23`; metal avg `0.3121` n `18`; unknown avg `0.1679` n `687`
- 4h: commodity avg `-0.5023` n `12`; crypto_alt avg `0.5944` n `228`; crypto_major avg `0.9507` n `8`; equity avg `-0.3201` n `77`; fx avg `0.0212` n `6`; index avg `-0.005` n `23`; metal avg `0.3911` n `18`; unknown avg `0.5791` n `687`
- 24h: commodity avg `-0.5901` n `12`; crypto_alt avg `0.4307` n `228`; crypto_major avg `2.2345` n `8`; equity avg `1.4859` n `76`; fx avg `-0.0667` n `6`; index avg `0.4015` n `23`; metal avg `0.15` n `18`; unknown avg `0.5521` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
