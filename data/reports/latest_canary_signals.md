# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T17:52:28.437144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0158` n `12`; crypto_alt avg `0.0086` n `228`; crypto_major avg `0.0828` n `8`; equity avg `0.0128` n `78`; fx avg `-0.0049` n `6`; index avg `-0.0041` n `23`; metal avg `0.0202` n `18`; unknown avg `-0.101` n `702`
- 1h: commodity avg `0.0403` n `12`; crypto_alt avg `-0.1529` n `228`; crypto_major avg `-0.1501` n `8`; equity avg `-0.0203` n `78`; fx avg `-0.0292` n `6`; index avg `-0.0094` n `23`; metal avg `0.0136` n `18`; unknown avg `0.1348` n `702`
- 4h: commodity avg `0.1672` n `12`; crypto_alt avg `0.0442` n `228`; crypto_major avg `0.2202` n `8`; equity avg `0.031` n `78`; fx avg `-0.0767` n `6`; index avg `-0.0242` n `23`; metal avg `0.022` n `18`; unknown avg `-0.7731` n `702`
- 24h: commodity avg `0.1869` n `12`; crypto_alt avg `1.6781` n `228`; crypto_major avg `0.4908` n `8`; equity avg `0.4377` n `78`; fx avg `-0.0755` n `6`; index avg `0.0114` n `23`; metal avg `0.0012` n `18`; unknown avg `-0.3394` n `653`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
