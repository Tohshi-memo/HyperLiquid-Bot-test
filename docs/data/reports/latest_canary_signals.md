# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T21:22:31.263214+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0349` n `12`; crypto_alt avg `0.0326` n `230`; crypto_major avg `0.088` n `8`; equity avg `0.0078` n `92`; fx avg `-0.0083` n `6`; index avg `0.0072` n `25`; metal avg `0.0113` n `20`; unknown avg `0.2079` n `768`
- 1h: commodity avg `-0.0455` n `12`; crypto_alt avg `0.1323` n `230`; crypto_major avg `0.2712` n `8`; equity avg `0.0588` n `92`; fx avg `-0.0073` n `6`; index avg `0.01` n `25`; metal avg `-0.0058` n `20`; unknown avg `-0.5172` n `768`
- 4h: commodity avg `0.1595` n `12`; crypto_alt avg `-0.056` n `230`; crypto_major avg `0.6014` n `8`; equity avg `0.2825` n `92`; fx avg `0.0068` n `6`; index avg `-0.0146` n `25`; metal avg `-0.0129` n `20`; unknown avg `-0.2115` n `766`
- 24h: commodity avg `0.2792` n `12`; crypto_alt avg `2.0774` n `230`; crypto_major avg `3.7876` n `8`; equity avg `1.4586` n `92`; fx avg `-0.0144` n `6`; index avg `0.4227` n `25`; metal avg `0.5918` n `20`; unknown avg `0.2416` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1703`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
