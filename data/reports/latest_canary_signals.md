# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T05:22:26.868825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0218` n `12`; crypto_alt avg `-0.153` n `230`; crypto_major avg `-0.1427` n `8`; equity avg `0.0037` n `92`; fx avg `0.0015` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0029` n `20`; unknown avg `-0.1047` n `765`
- 1h: commodity avg `0.0385` n `12`; crypto_alt avg `-0.314` n `230`; crypto_major avg `-0.289` n `8`; equity avg `-0.051` n `92`; fx avg `-0.0002` n `6`; index avg `-0.0088` n `25`; metal avg `-0.0028` n `20`; unknown avg `0.3835` n `765`
- 4h: commodity avg `-0.0444` n `12`; crypto_alt avg `0.2652` n `230`; crypto_major avg `-0.0267` n `8`; equity avg `0.0314` n `92`; fx avg `-0.0005` n `6`; index avg `-0.0035` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.4841` n `765`
- 24h: commodity avg `0.5191` n `12`; crypto_alt avg `-0.4574` n `230`; crypto_major avg `-0.5631` n `8`; equity avg `0.0523` n `92`; fx avg `0.0012` n `6`; index avg `-0.1038` n `25`; metal avg `-0.0891` n `20`; unknown avg `-0.0483` n `729`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
