# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T22:07:33.972286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0358` n `12`; crypto_alt avg `-0.1981` n `228`; crypto_major avg `0.0163` n `8`; equity avg `-0.2853` n `74`; fx avg `-0.0414` n `6`; index avg `-0.1237` n `23`; metal avg `-0.3817` n `18`; unknown avg `0.1809` n `550`
- 1h: commodity avg `0.0884` n `12`; crypto_alt avg `-0.7493` n `228`; crypto_major avg `-0.4933` n `8`; equity avg `-0.3419` n `74`; fx avg `-0.0296` n `6`; index avg `-0.1375` n `23`; metal avg `-0.4027` n `18`; unknown avg `0.1134` n `550`
- 4h: commodity avg `0.3388` n `12`; crypto_alt avg `-2.3778` n `228`; crypto_major avg `-1.6497` n `8`; equity avg `-2.0289` n `74`; fx avg `-0.0932` n `6`; index avg `-0.9548` n `23`; metal avg `-1.6441` n `18`; unknown avg `0.2238` n `550`
- 24h: commodity avg `1.3138` n `12`; crypto_alt avg `-3.1511` n `228`; crypto_major avg `-2.9545` n `8`; equity avg `-2.5058` n `74`; fx avg `-0.0775` n `6`; index avg `-1.8314` n `23`; metal avg `-2.9203` n `18`; unknown avg `-0.4323` n `537`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
