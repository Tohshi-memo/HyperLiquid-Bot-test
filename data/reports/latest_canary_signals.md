# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T23:37:25.650020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `13`; crypto_alt avg `0.4241` n `237`; crypto_major avg `0.3866` n `8`; equity avg `0.1605` n `154`; fx avg `0.0019` n `6`; index avg `0.0403` n `27`; metal avg `0.0039` n `20`; unknown avg `66.1865` n `1238`
- 1h: commodity avg `0.0176` n `13`; crypto_alt avg `0.5417` n `237`; crypto_major avg `0.471` n `8`; equity avg `-0.0031` n `154`; fx avg `-0.0193` n `6`; index avg `0.0204` n `27`; metal avg `-0.0109` n `20`; unknown avg `43.6416` n `1228`
- 4h: commodity avg `-0.158` n `13`; crypto_alt avg `0.2223` n `237`; crypto_major avg `0.0544` n `8`; equity avg `0.0535` n `154`; fx avg `-0.0263` n `6`; index avg `0.0412` n `27`; metal avg `-0.0028` n `20`; unknown avg `41.5608` n `1116`
- 24h: commodity avg `-0.0773` n `13`; crypto_alt avg `0.2459` n `237`; crypto_major avg `0.3361` n `8`; equity avg `0.8438` n `153`; fx avg `-0.0078` n `6`; index avg `-0.0398` n `27`; metal avg `-0.0594` n `20`; unknown avg `760.8159` n `972`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2201`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
