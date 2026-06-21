# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T10:07:29.975423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0121` n `12`; crypto_alt avg `0.0425` n `228`; crypto_major avg `0.0296` n `8`; equity avg `0.0127` n `78`; fx avg `0.0071` n `6`; index avg `0.0013` n `23`; metal avg `0.0015` n `18`; unknown avg `0.0657` n `702`
- 1h: commodity avg `-0.0298` n `12`; crypto_alt avg `0.4702` n `228`; crypto_major avg `0.46` n `8`; equity avg `0.0599` n `78`; fx avg `0.0011` n `6`; index avg `0.0119` n `23`; metal avg `0.0212` n `18`; unknown avg `0.0504` n `702`
- 4h: commodity avg `-0.0598` n `12`; crypto_alt avg `0.7664` n `228`; crypto_major avg `0.0191` n `8`; equity avg `0.0223` n `78`; fx avg `-0.0034` n `6`; index avg `0.0157` n `23`; metal avg `0.0139` n `18`; unknown avg `-0.1881` n `694`
- 24h: commodity avg `0.047` n `12`; crypto_alt avg `1.2118` n `228`; crypto_major avg `-0.0878` n `8`; equity avg `0.317` n `78`; fx avg `0.0414` n `6`; index avg `0.0221` n `23`; metal avg `-0.0034` n `18`; unknown avg `0.1322` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
