# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T03:07:30.014061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `13`; crypto_alt avg `-0.0885` n `239`; crypto_major avg `-0.1566` n `8`; equity avg `-0.0614` n `160`; fx avg `0.0023` n `6`; index avg `-0.0258` n `27`; metal avg `0.0115` n `20`; unknown avg `0.0691` n `1257`
- 1h: commodity avg `-0.1035` n `13`; crypto_alt avg `-0.0673` n `239`; crypto_major avg `-0.1052` n `8`; equity avg `0.0053` n `160`; fx avg `-0.0002` n `6`; index avg `-0.033` n `27`; metal avg `-0.0394` n `20`; unknown avg `0.1838` n `1255`
- 4h: commodity avg `-0.1252` n `13`; crypto_alt avg `-0.3529` n `239`; crypto_major avg `-0.4912` n `8`; equity avg `-0.2534` n `160`; fx avg `0.0562` n `6`; index avg `-0.1188` n `27`; metal avg `-0.0883` n `20`; unknown avg `0.1855` n `1247`
- 24h: commodity avg `-0.7336` n `13`; crypto_alt avg `0.3938` n `239`; crypto_major avg `-0.5896` n `8`; equity avg `3.3783` n `160`; fx avg `0.0378` n `6`; index avg `0.3265` n `27`; metal avg `0.0899` n `20`; unknown avg `183.805` n `1070`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
