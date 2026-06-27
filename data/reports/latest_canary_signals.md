# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T22:22:31.405603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0338` n `12`; crypto_alt avg `-0.1239` n `228`; crypto_major avg `-0.1362` n `8`; equity avg `-0.0081` n `88`; fx avg `0.0094` n `6`; index avg `-0.0154` n `23`; metal avg `-0.0176` n `20`; unknown avg `-0.2082` n `764`
- 1h: commodity avg `0.2104` n `12`; crypto_alt avg `-0.6519` n `228`; crypto_major avg `-0.673` n `8`; equity avg `-0.0648` n `88`; fx avg `0.0042` n `6`; index avg `-0.0665` n `23`; metal avg `-0.0287` n `20`; unknown avg `-0.2702` n `764`
- 4h: commodity avg `0.1579` n `12`; crypto_alt avg `-0.8618` n `228`; crypto_major avg `-0.9874` n `8`; equity avg `-0.0653` n `88`; fx avg `0.0048` n `6`; index avg `-0.0681` n `23`; metal avg `-0.0566` n `20`; unknown avg `-0.3586` n `764`
- 24h: commodity avg `0.1978` n `12`; crypto_alt avg `-0.6217` n `228`; crypto_major avg `-0.8347` n `8`; equity avg `0.3561` n `88`; fx avg `0.0306` n `6`; index avg `-0.0438` n `23`; metal avg `-0.0278` n `20`; unknown avg `-0.6518` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.208`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
