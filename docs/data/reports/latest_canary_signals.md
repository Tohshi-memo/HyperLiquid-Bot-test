# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T15:26:58.759152+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0205` n `12`; crypto_alt avg `0.0354` n `230`; crypto_major avg `0.1495` n `8`; equity avg `0.0384` n `92`; fx avg `-0.0103` n `6`; index avg `0.0156` n `25`; metal avg `0.009` n `20`; unknown avg `-0.0466` n `765`
- 1h: commodity avg `0.0195` n `12`; crypto_alt avg `0.2427` n `230`; crypto_major avg `0.4251` n `8`; equity avg `0.1076` n `92`; fx avg `-0.0168` n `6`; index avg `0.0269` n `25`; metal avg `-0.0111` n `20`; unknown avg `0.1468` n `765`
- 4h: commodity avg `0.0134` n `12`; crypto_alt avg `0.7482` n `230`; crypto_major avg `0.7529` n `8`; equity avg `-0.0193` n `92`; fx avg `-0.0265` n `6`; index avg `0.0229` n `25`; metal avg `-0.0252` n `20`; unknown avg `0.1462` n `765`
- 24h: commodity avg `0.1167` n `12`; crypto_alt avg `1.1783` n `229`; crypto_major avg `0.9174` n `8`; equity avg `0.3712` n `92`; fx avg `-0.0493` n `6`; index avg `0.0943` n `25`; metal avg `0.081` n `20`; unknown avg `3.0223` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
