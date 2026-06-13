# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T04:22:28.480319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0305` n `12`; crypto_alt avg `0.1298` n `228`; crypto_major avg `0.0603` n `8`; equity avg `0.008` n `74`; fx avg `-0.0022` n `6`; index avg `0.0252` n `23`; metal avg `-0.0192` n `18`; unknown avg `0.452` n `643`
- 1h: commodity avg `0.1494` n `12`; crypto_alt avg `0.0703` n `228`; crypto_major avg `-0.0427` n `8`; equity avg `-0.1521` n `74`; fx avg `0.0005` n `6`; index avg `-0.0024` n `23`; metal avg `-0.0514` n `18`; unknown avg `1.1876` n `643`
- 4h: commodity avg `0.0001` n `12`; crypto_alt avg `0.2258` n `228`; crypto_major avg `-0.2399` n `8`; equity avg `-0.2581` n `74`; fx avg `-0.0093` n `6`; index avg `0.0616` n `23`; metal avg `-0.0658` n `18`; unknown avg `-0.0328` n `643`
- 24h: commodity avg `-0.5488` n `12`; crypto_alt avg `-0.0911` n `228`; crypto_major avg `-0.5179` n `8`; equity avg `-0.8372` n `74`; fx avg `-0.0123` n `6`; index avg `0.575` n `23`; metal avg `0.4137` n `18`; unknown avg `39.9275` n `515`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
