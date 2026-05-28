# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T03:37:17.258605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1014` n `12`; crypto_alt avg `-0.632` n `228`; crypto_major avg `-0.4252` n `8`; equity avg `-0.579` n `67`; fx avg `-0.0086` n `6`; index avg `-0.2755` n `23`; metal avg `-0.167` n `18`; unknown avg `15.3301` n `419`
- 1h: commodity avg `0.6657` n `12`; crypto_alt avg `-1.3648` n `228`; crypto_major avg `-0.8761` n `8`; equity avg `-1.0249` n `67`; fx avg `-0.0198` n `6`; index avg `-0.4389` n `23`; metal avg `-0.7382` n `18`; unknown avg `-0.2586` n `419`
- 4h: commodity avg `0.7528` n `12`; crypto_alt avg `-1.495` n `228`; crypto_major avg `-0.9444` n `8`; equity avg `-1.4516` n `67`; fx avg `-0.0115` n `6`; index avg `-0.5777` n `23`; metal avg `-1.6273` n `18`; unknown avg `-0.322` n `419`
- 24h: commodity avg `0.0875` n `12`; crypto_alt avg `-3.5922` n `228`; crypto_major avg `-2.8376` n `8`; equity avg `-1.956` n `67`; fx avg `-0.0653` n `6`; index avg `-1.2305` n `23`; metal avg `-2.6782` n `18`; unknown avg `-1.0341` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
