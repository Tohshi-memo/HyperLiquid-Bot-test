# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T04:22:24.530747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `-0.0355` n `230`; crypto_major avg `-0.1033` n `8`; equity avg `-0.0036` n `92`; fx avg `0.0006` n `6`; index avg `0.0122` n `25`; metal avg `0.0041` n `20`; unknown avg `0.1674` n `765`
- 1h: commodity avg `0.03` n `12`; crypto_alt avg `0.1754` n `230`; crypto_major avg `0.0487` n `8`; equity avg `0.0007` n `92`; fx avg `0.0021` n `6`; index avg `0.0278` n `25`; metal avg `-0.0035` n `20`; unknown avg `-0.3623` n `765`
- 4h: commodity avg `-0.1527` n `12`; crypto_alt avg `0.7913` n `230`; crypto_major avg `0.4778` n `8`; equity avg `0.0629` n `92`; fx avg `-0.0001` n `6`; index avg `-0.018` n `25`; metal avg `-0.0133` n `20`; unknown avg `-0.0936` n `765`
- 24h: commodity avg `0.4093` n `12`; crypto_alt avg `-0.3728` n `229`; crypto_major avg `-0.3315` n `8`; equity avg `0.0819` n `92`; fx avg `0.0196` n `6`; index avg `-0.0893` n `25`; metal avg `-0.0902` n `20`; unknown avg `-0.041` n `729`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
