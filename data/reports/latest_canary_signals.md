# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T14:52:28.137433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `13`; crypto_alt avg `-0.0142` n `238`; crypto_major avg `-0.0346` n `8`; equity avg `0.1993` n `154`; fx avg `-0.0101` n `6`; index avg `0.0303` n `27`; metal avg `0.0384` n `20`; unknown avg `0.7711` n `1236`
- 1h: commodity avg `-0.1773` n `13`; crypto_alt avg `0.4429` n `238`; crypto_major avg `0.3392` n `8`; equity avg `0.6867` n `154`; fx avg `-0.0131` n `6`; index avg `0.1215` n `27`; metal avg `0.2449` n `20`; unknown avg `-0.1075` n `1166`
- 4h: commodity avg `-0.2495` n `13`; crypto_alt avg `0.6186` n `238`; crypto_major avg `0.6551` n `8`; equity avg `1.2065` n `154`; fx avg `0.0048` n `6`; index avg `0.1138` n `27`; metal avg `0.3602` n `20`; unknown avg `0.5402` n `1114`
- 24h: commodity avg `-0.4039` n `13`; crypto_alt avg `-0.305` n `237`; crypto_major avg `0.3587` n `8`; equity avg `1.2229` n `154`; fx avg `-0.0677` n `6`; index avg `0.2669` n `27`; metal avg `0.0411` n `20`; unknown avg `383.4167` n `1058`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1951`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1917`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
