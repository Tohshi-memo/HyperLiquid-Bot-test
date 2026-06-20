# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T13:11:07.584547+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0761` n `12`; crypto_alt avg `0.0739` n `228`; crypto_major avg `0.076` n `8`; equity avg `0.0656` n `78`; fx avg `0.0` n `6`; index avg `0.0059` n `23`; metal avg `0.0046` n `18`; unknown avg `-0.175` n `701`
- 1h: commodity avg `0.0626` n `12`; crypto_alt avg `-0.2652` n `228`; crypto_major avg `-0.261` n `8`; equity avg `0.024` n `78`; fx avg `-0.0027` n `6`; index avg `0.0116` n `23`; metal avg `0.0052` n `18`; unknown avg `0.2635` n `701`
- 4h: commodity avg `-0.0081` n `12`; crypto_alt avg `-0.2291` n `228`; crypto_major avg `0.0418` n `8`; equity avg `-0.0246` n `78`; fx avg `0.3219` n `6`; index avg `0.0238` n `23`; metal avg `0.0221` n `18`; unknown avg `-0.3238` n `573`
- 24h: commodity avg `0.4929` n `12`; crypto_alt avg `-3.2543` n `228`; crypto_major avg `-3.4345` n `8`; equity avg `1.2028` n `78`; fx avg `-0.0677` n `6`; index avg `0.3035` n `23`; metal avg `-4.0878` n `18`; unknown avg `-0.2394` n `492`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
