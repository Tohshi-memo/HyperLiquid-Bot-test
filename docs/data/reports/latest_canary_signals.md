# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T23:22:31.273461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `13`; crypto_alt avg `0.2789` n `235`; crypto_major avg `0.0691` n `8`; equity avg `-0.0077` n `143`; fx avg `-0.011` n `6`; index avg `-0.0017` n `26`; metal avg `0.004` n `20`; unknown avg `0.0381` n `1079`
- 1h: commodity avg `-0.0338` n `13`; crypto_alt avg `0.3401` n `235`; crypto_major avg `0.011` n `8`; equity avg `0.0308` n `143`; fx avg `-0.0052` n `6`; index avg `-0.0022` n `26`; metal avg `0.0035` n `20`; unknown avg `0.3282` n `1077`
- 4h: commodity avg `0.0699` n `13`; crypto_alt avg `0.6948` n `235`; crypto_major avg `-0.0003` n `8`; equity avg `0.1101` n `143`; fx avg `0.0185` n `6`; index avg `0.0017` n `26`; metal avg `0.0072` n `20`; unknown avg `0.2487` n `1054`
- 24h: commodity avg `-0.0378` n `13`; crypto_alt avg `2.2498` n `235`; crypto_major avg `0.8744` n `8`; equity avg `0.2306` n `143`; fx avg `-0.0179` n `6`; index avg `0.0514` n `26`; metal avg `-0.0218` n `20`; unknown avg `0.111` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1998`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
