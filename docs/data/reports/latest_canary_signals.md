# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T17:07:41.726498+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0955` n `12`; crypto_alt avg `0.2203` n `228`; crypto_major avg `0.2503` n `8`; equity avg `-0.0141` n `74`; fx avg `-0.0026` n `6`; index avg `-0.0612` n `23`; metal avg `0.0102` n `18`; unknown avg `0.2949` n `548`
- 1h: commodity avg `-0.0158` n `12`; crypto_alt avg `-0.8375` n `228`; crypto_major avg `-0.9369` n `8`; equity avg `-0.4388` n `74`; fx avg `0.0248` n `6`; index avg `-0.2943` n `23`; metal avg `-0.1578` n `18`; unknown avg `4.7984` n `548`
- 4h: commodity avg `0.4871` n `12`; crypto_alt avg `0.3219` n `228`; crypto_major avg `0.4929` n `8`; equity avg `0.4019` n `74`; fx avg `0.0119` n `6`; index avg `-0.3593` n `23`; metal avg `-0.1124` n `18`; unknown avg `2.9526` n `547`
- 24h: commodity avg `1.4074` n `12`; crypto_alt avg `0.5` n `228`; crypto_major avg `-0.6134` n `8`; equity avg `1.0122` n `74`; fx avg `-0.029` n `6`; index avg `0.4376` n `23`; metal avg `-1.0321` n `18`; unknown avg `0.1697` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1105`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0905`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0704`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0642`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0611`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0583`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0581`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0553`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0484`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0466`, n `669`, weak_sample_signal
