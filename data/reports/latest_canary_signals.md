# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T14:07:34.288420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0343` n `13`; crypto_alt avg `0.1525` n `238`; crypto_major avg `0.1502` n `8`; equity avg `0.2594` n `154`; fx avg `0.0177` n `6`; index avg `0.0397` n `27`; metal avg `0.1218` n `20`; unknown avg `-0.1411` n `1164`
- 1h: commodity avg `-0.0405` n `13`; crypto_alt avg `-0.0291` n `238`; crypto_major avg `0.0348` n `8`; equity avg `0.3591` n `154`; fx avg `-0.001` n `6`; index avg `-0.016` n `27`; metal avg `0.1192` n `20`; unknown avg `0.3709` n `1164`
- 4h: commodity avg `-0.2312` n `13`; crypto_alt avg `0.9303` n `238`; crypto_major avg `1.0452` n `8`; equity avg `1.2348` n `154`; fx avg `0.021` n `6`; index avg `0.1134` n `27`; metal avg `0.2796` n `20`; unknown avg `1.2212` n `1114`
- 24h: commodity avg `-0.1` n `13`; crypto_alt avg `0.238` n `237`; crypto_major avg `0.8707` n `8`; equity avg `2.2325` n `154`; fx avg `-0.0012` n `6`; index avg `0.401` n `27`; metal avg `0.1402` n `20`; unknown avg `1339.4665` n `1038`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1902`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
