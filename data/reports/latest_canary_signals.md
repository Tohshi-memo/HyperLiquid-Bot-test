# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T07:52:29.758585+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0274` n `12`; crypto_alt avg `-0.0231` n `230`; crypto_major avg `-0.0259` n `8`; equity avg `-0.032` n `92`; fx avg `0.0021` n `6`; index avg `-0.0007` n `25`; metal avg `-0.0061` n `20`; unknown avg `-0.2336` n `765`
- 1h: commodity avg `0.0925` n `12`; crypto_alt avg `0.0474` n `230`; crypto_major avg `0.1393` n `8`; equity avg `-0.013` n `92`; fx avg `0.012` n `6`; index avg `0.012` n `25`; metal avg `-0.0057` n `20`; unknown avg `0.1753` n `763`
- 4h: commodity avg `0.1404` n `12`; crypto_alt avg `-0.6427` n `230`; crypto_major avg `-0.5242` n `8`; equity avg `-0.2032` n `92`; fx avg `0.0028` n `6`; index avg `-0.0018` n `25`; metal avg `-0.0249` n `20`; unknown avg `0.1842` n `747`
- 24h: commodity avg `0.5216` n `12`; crypto_alt avg `-0.7752` n `230`; crypto_major avg `-0.7554` n `8`; equity avg `-0.201` n `92`; fx avg `-0.0024` n `6`; index avg `-0.1254` n `25`; metal avg `-0.0938` n `20`; unknown avg `-0.0454` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.178`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
