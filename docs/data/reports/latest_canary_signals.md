# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T22:07:17.302768+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0944` n `12`; crypto_alt avg `0.4529` n `228`; crypto_major avg `0.4089` n `8`; equity avg `-0.0338` n `67`; fx avg `-0.0201` n `6`; index avg `0.0295` n `23`; metal avg `0.1815` n `18`; unknown avg `0.2501` n `419`
- 1h: commodity avg `-0.0012` n `12`; crypto_alt avg `-1.5737` n `228`; crypto_major avg `-0.8349` n `8`; equity avg `-0.0776` n `67`; fx avg `-0.0261` n `6`; index avg `-0.004` n `23`; metal avg `0.1037` n `18`; unknown avg `0.1265` n `419`
- 4h: commodity avg `-0.2723` n `12`; crypto_alt avg `-0.8779` n `228`; crypto_major avg `-0.2146` n `8`; equity avg `0.2562` n `67`; fx avg `-0.0031` n `6`; index avg `0.2177` n `23`; metal avg `0.3101` n `18`; unknown avg `-0.2365` n `418`
- 24h: commodity avg `-1.1425` n `12`; crypto_alt avg `-1.5379` n `228`; crypto_major avg `-0.6115` n `8`; equity avg `-0.223` n `67`; fx avg `-0.1055` n `6`; index avg `-0.3694` n `23`; metal avg `-1.2104` n `18`; unknown avg `-0.3664` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
