# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T13:22:16.572426+00:00`
- Correlation status: `ready`
- Asset price records: `553`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.053` n `12`; crypto_alt avg `0.0881` n `228`; crypto_major avg `0.0641` n `8`; equity avg `0.1277` n `65`; fx avg `-0.0077` n `5`; index avg `0.0546` n `23`; metal avg `-0.1288` n `18`; unknown avg `-0.1918` n `365`
- 1h: commodity avg `-0.0998` n `12`; crypto_alt avg `0.2128` n `228`; crypto_major avg `-0.0463` n `8`; equity avg `0.0707` n `65`; fx avg `0.011` n `5`; index avg `-0.0556` n `23`; metal avg `-0.1366` n `18`; unknown avg `0.0188` n `365`
- 4h: commodity avg `-0.6169` n `12`; crypto_alt avg `0.6135` n `228`; crypto_major avg `0.0021` n `8`; equity avg `-0.0772` n `65`; fx avg `-0.0085` n `5`; index avg `-0.1708` n `23`; metal avg `0.3587` n `18`; unknown avg `0.2298` n `357`
- 24h: commodity avg `-1.8578` n `12`; crypto_alt avg `1.3068` n `228`; crypto_major avg `-1.3226` n `8`; equity avg `1.6399` n `65`; fx avg `0.0844` n `5`; index avg `0.9282` n `23`; metal avg `2.2739` n `18`; unknown avg `0.4629` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1338`, n `549`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1253`, n `549`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1083`, n `549`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0788`, n `545`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.076`, n `545`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0752`, n `545`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0747`, n `545`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0728`, n `549`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0704`, n `545`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.064`, n `549`, weak_sample_signal
