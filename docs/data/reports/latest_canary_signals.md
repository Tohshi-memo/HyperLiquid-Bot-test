# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T11:37:29.508215+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.026` n `13`; crypto_alt avg `-0.1026` n `238`; crypto_major avg `-0.0739` n `8`; equity avg `-0.0841` n `154`; fx avg `-0.0047` n `6`; index avg `-0.0234` n `27`; metal avg `0.005` n `20`; unknown avg `0.1071` n `1236`
- 1h: commodity avg `-0.2299` n `13`; crypto_alt avg `0.3906` n `238`; crypto_major avg `0.3359` n `8`; equity avg `0.6529` n `154`; fx avg `-0.0134` n `6`; index avg `0.0863` n `27`; metal avg `0.0966` n `20`; unknown avg `9.0039` n `1188`
- 4h: commodity avg `-0.3011` n `13`; crypto_alt avg `-0.2586` n `238`; crypto_major avg `0.151` n `8`; equity avg `1.1498` n `154`; fx avg `-0.0077` n `6`; index avg `0.1567` n `27`; metal avg `0.1601` n `20`; unknown avg `14.9235` n `1156`
- 24h: commodity avg `-0.2222` n `13`; crypto_alt avg `-0.4335` n `237`; crypto_major avg `-0.1275` n `8`; equity avg `1.3647` n `153`; fx avg `-0.0517` n `6`; index avg `0.3893` n `27`; metal avg `-0.221` n `20`; unknown avg `1050.8531` n `1038`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1944`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1894`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
