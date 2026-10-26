# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T21:42:53.986067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0088` n `13`; crypto_alt avg `0.3483` n `237`; crypto_major avg `0.1371` n `8`; equity avg `0.0797` n `154`; fx avg `-0.0013` n `6`; index avg `0.0057` n `27`; metal avg `0.0094` n `20`; unknown avg `0.1607` n `1236`
- 1h: commodity avg `-0.0261` n `13`; crypto_alt avg `0.1581` n `237`; crypto_major avg `0.1292` n `8`; equity avg `0.1343` n `154`; fx avg `-0.0049` n `6`; index avg `0.0151` n `27`; metal avg `0.0257` n `20`; unknown avg `2.0602` n `1226`
- 4h: commodity avg `-0.2084` n `13`; crypto_alt avg `-0.7063` n `237`; crypto_major avg `-0.6755` n `8`; equity avg `-0.1818` n `154`; fx avg `-0.039` n `6`; index avg `-0.0264` n `27`; metal avg `-0.0711` n `20`; unknown avg `9.7916` n `1134`
- 24h: commodity avg `-0.3661` n `13`; crypto_alt avg `-0.2874` n `237`; crypto_major avg `-0.1477` n `8`; equity avg `0.7017` n `153`; fx avg `-0.0175` n `6`; index avg `-0.0922` n `27`; metal avg `0.0147` n `20`; unknown avg `704.1966` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
