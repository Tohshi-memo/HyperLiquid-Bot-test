# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T19:22:32.863011+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0221` n `12`; crypto_alt avg `0.0585` n `228`; crypto_major avg `0.0179` n `8`; equity avg `-0.1332` n `85`; fx avg `0.0112` n `6`; index avg `0.0082` n `23`; metal avg `-0.0168` n `20`; unknown avg `-0.236` n `717`
- 1h: commodity avg `0.0833` n `12`; crypto_alt avg `-0.7009` n `228`; crypto_major avg `-0.8936` n `8`; equity avg `-0.6834` n `85`; fx avg `0.0004` n `6`; index avg `-0.0499` n `23`; metal avg `-0.0041` n `20`; unknown avg `0.1409` n `717`
- 4h: commodity avg `0.0393` n `12`; crypto_alt avg `-1.0377` n `228`; crypto_major avg `-0.769` n `8`; equity avg `-0.3821` n `85`; fx avg `-0.0062` n `6`; index avg `-0.0586` n `23`; metal avg `-0.0496` n `20`; unknown avg `-0.3719` n `716`
- 24h: commodity avg `-0.9883` n `12`; crypto_alt avg `-0.9701` n `228`; crypto_major avg `-0.4653` n `8`; equity avg `-0.842` n `85`; fx avg `0.05` n `6`; index avg `0.0688` n `23`; metal avg `0.2954` n `18`; unknown avg `0.5422` n `639`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
