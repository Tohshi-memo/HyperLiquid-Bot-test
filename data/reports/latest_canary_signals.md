# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T23:37:29.093111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0238` n `12`; crypto_alt avg `0.1785` n `228`; crypto_major avg `0.1186` n `8`; equity avg `0.342` n `74`; fx avg `0.0309` n `6`; index avg `0.0828` n `23`; metal avg `0.4054` n `18`; unknown avg `0.0319` n `550`
- 1h: commodity avg `0.1178` n `12`; crypto_alt avg `0.5297` n `228`; crypto_major avg `0.3807` n `8`; equity avg `-0.1137` n `74`; fx avg `0.0227` n `6`; index avg `-0.0027` n `23`; metal avg `-0.1563` n `18`; unknown avg `0.0111` n `550`
- 4h: commodity avg `0.6784` n `12`; crypto_alt avg `-0.8527` n `228`; crypto_major avg `-0.7106` n `8`; equity avg `-1.3687` n `74`; fx avg `-0.0528` n `6`; index avg `-0.3525` n `23`; metal avg `-0.7041` n `18`; unknown avg `0.1033` n `550`
- 24h: commodity avg `1.5645` n `12`; crypto_alt avg `-2.0587` n `228`; crypto_major avg `-2.0153` n `8`; equity avg `-2.1848` n `74`; fx avg `-0.0518` n `6`; index avg `-1.6139` n `23`; metal avg `-2.3275` n `18`; unknown avg `-0.3209` n `537`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
