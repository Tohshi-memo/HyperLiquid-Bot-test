# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T09:37:31.453939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0342` n `12`; crypto_alt avg `-0.0441` n `228`; crypto_major avg `-0.0213` n `8`; equity avg `0.003` n `79`; fx avg `0.004` n `6`; index avg `-0.0013` n `23`; metal avg `0.0137` n `18`; unknown avg `0.0017` n `701`
- 1h: commodity avg `-0.0188` n `12`; crypto_alt avg `0.117` n `228`; crypto_major avg `0.0812` n `8`; equity avg `0.1294` n `79`; fx avg `0.0263` n `6`; index avg `0.0339` n `23`; metal avg `0.1908` n `18`; unknown avg `-0.0423` n `701`
- 4h: commodity avg `0.1032` n `12`; crypto_alt avg `0.0357` n `228`; crypto_major avg `0.2081` n `8`; equity avg `0.4147` n `79`; fx avg `0.0364` n `6`; index avg `0.0568` n `23`; metal avg `0.1132` n `18`; unknown avg `0.2344` n `661`
- 24h: commodity avg `-0.2048` n `12`; crypto_alt avg `-0.2537` n `228`; crypto_major avg `-0.1194` n `8`; equity avg `-0.1896` n `79`; fx avg `0.0456` n `6`; index avg `0.0322` n `23`; metal avg `0.4911` n `18`; unknown avg `-0.0131` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
