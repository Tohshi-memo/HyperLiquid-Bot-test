# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T03:22:26.819082+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `13`; crypto_alt avg `0.2191` n `239`; crypto_major avg `0.0571` n `8`; equity avg `0.1328` n `161`; fx avg `0.0158` n `6`; index avg `0.0197` n `27`; metal avg `0.0121` n `20`; unknown avg `0.451` n `1261`
- 1h: commodity avg `0.006` n `13`; crypto_alt avg `0.922` n `239`; crypto_major avg `0.8154` n `8`; equity avg `0.7016` n `161`; fx avg `-0.0255` n `6`; index avg `0.0675` n `27`; metal avg `0.1173` n `20`; unknown avg `4.8822` n `1255`
- 4h: commodity avg `0.0789` n `13`; crypto_alt avg `0.8626` n `239`; crypto_major avg `0.5229` n `8`; equity avg `1.8433` n `161`; fx avg `-0.0765` n `6`; index avg `0.2181` n `27`; metal avg `0.2964` n `20`; unknown avg `24.7805` n `1249`
- 24h: commodity avg `0.3136` n `13`; crypto_alt avg `0.3388` n `239`; crypto_major avg `-1.6355` n `8`; equity avg `1.2348` n `161`; fx avg `-0.2355` n `6`; index avg `0.1831` n `27`; metal avg `-0.27` n `20`; unknown avg `24.7614` n `1172`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.309`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2787`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
