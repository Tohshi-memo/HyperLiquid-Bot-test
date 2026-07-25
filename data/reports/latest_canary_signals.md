# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T08:07:25.936320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `12`; crypto_alt avg `-0.2263` n `230`; crypto_major avg `-0.153` n `8`; equity avg `-0.0267` n `100`; fx avg `-0.0002` n `6`; index avg `0.0119` n `25`; metal avg `-0.0058` n `20`; unknown avg `0.0101` n `774`
- 1h: commodity avg `-0.0075` n `12`; crypto_alt avg `-0.3219` n `230`; crypto_major avg `-0.2391` n `8`; equity avg `-0.0499` n `100`; fx avg `0.0077` n `6`; index avg `0.0062` n `25`; metal avg `0.0041` n `20`; unknown avg `-0.2162` n `774`
- 4h: commodity avg `0.075` n `12`; crypto_alt avg `-0.5856` n `230`; crypto_major avg `-0.4229` n `8`; equity avg `-0.0821` n `100`; fx avg `0.0218` n `6`; index avg `0.0262` n `25`; metal avg `0.0079` n `20`; unknown avg `-0.2678` n `758`
- 24h: commodity avg `-0.1563` n `12`; crypto_alt avg `-2.0699` n `230`; crypto_major avg `-1.8553` n `8`; equity avg `-2.6813` n `100`; fx avg `-0.0588` n `6`; index avg `-0.1913` n `25`; metal avg `0.0167` n `20`; unknown avg `13.4049` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1147`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1072`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `666`, weak_sample_signal
