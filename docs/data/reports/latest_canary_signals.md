# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T12:22:30.520729+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `13`; crypto_alt avg `0.3849` n `238`; crypto_major avg `0.3033` n `8`; equity avg `0.1487` n `154`; fx avg `0.0023` n `6`; index avg `0.0314` n `27`; metal avg `0.0098` n `20`; unknown avg `0.2981` n `1236`
- 1h: commodity avg `0.0872` n `13`; crypto_alt avg `0.0864` n `238`; crypto_major avg `0.1909` n `8`; equity avg `0.0179` n `154`; fx avg `0.029` n `6`; index avg `0.0186` n `27`; metal avg `-0.0053` n `20`; unknown avg `-0.1049` n `1226`
- 4h: commodity avg `-0.3202` n `13`; crypto_alt avg `-0.1129` n `238`; crypto_major avg `0.2183` n `8`; equity avg `0.8843` n `154`; fx avg `0.0016` n `6`; index avg `0.1603` n `27`; metal avg `0.1247` n `20`; unknown avg `14.3606` n `1180`
- 24h: commodity avg `-0.1465` n `13`; crypto_alt avg `-0.3453` n `237`; crypto_major avg `0.0318` n `8`; equity avg `0.8234` n `153`; fx avg `-0.0287` n `6`; index avg `0.3409` n `27`; metal avg `-0.2964` n `20`; unknown avg `1020.8724` n `1038`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1884`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
