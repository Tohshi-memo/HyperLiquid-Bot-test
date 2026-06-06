# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T09:37:24.497999+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1541` n `12`; crypto_alt avg `0.4232` n `228`; crypto_major avg `0.4299` n `8`; equity avg `-1.4861` n `74`; fx avg `0.0004` n `6`; index avg `-0.1009` n `23`; metal avg `-0.0163` n `18`; unknown avg `0.0724` n `425`
- 1h: commodity avg `0.0012` n `12`; crypto_alt avg `0.3985` n `228`; crypto_major avg `0.0956` n `8`; equity avg `0.3652` n `74`; fx avg `-0.0059` n `6`; index avg `0.413` n `23`; metal avg `0.033` n `18`; unknown avg `0.0768` n `425`
- 4h: commodity avg `-0.2642` n `12`; crypto_alt avg `2.4982` n `228`; crypto_major avg `1.7111` n `8`; equity avg `0.2986` n `74`; fx avg `-0.0133` n `6`; index avg `0.4945` n `23`; metal avg `0.2979` n `18`; unknown avg `0.4085` n `415`
- 24h: commodity avg `-1.3051` n `12`; crypto_alt avg `-2.9962` n `228`; crypto_major avg `-2.7548` n `8`; equity avg `-6.6321` n `74`; fx avg `-0.2453` n `6`; index avg `-3.8984` n `23`; metal avg `-4.1645` n `18`; unknown avg `0.8535` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
