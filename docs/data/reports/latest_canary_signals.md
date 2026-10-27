# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T04:22:25.945520+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.021` n `13`; crypto_alt avg `0.0595` n `237`; crypto_major avg `0.0334` n `8`; equity avg `-0.0156` n `154`; fx avg `-0.0059` n `6`; index avg `-0.0559` n `27`; metal avg `0.0248` n `20`; unknown avg `-0.094` n `1238`
- 1h: commodity avg `-0.0108` n `13`; crypto_alt avg `0.1685` n `237`; crypto_major avg `0.1098` n `8`; equity avg `-0.426` n `154`; fx avg `-0.0216` n `6`; index avg `-0.0146` n `27`; metal avg `0.1211` n `20`; unknown avg `73.2431` n `1224`
- 4h: commodity avg `-0.0322` n `13`; crypto_alt avg `-0.9842` n `237`; crypto_major avg `-0.6111` n `8`; equity avg `-1.1107` n `154`; fx avg `0.018` n `6`; index avg `-0.1059` n `27`; metal avg `-0.0355` n `20`; unknown avg `240.4506` n `1218`
- 24h: commodity avg `0.0527` n `13`; crypto_alt avg `0.2612` n `237`; crypto_major avg `0.6156` n `8`; equity avg `1.1327` n `153`; fx avg `-0.0075` n `6`; index avg `0.0185` n `27`; metal avg `-0.0437` n `20`; unknown avg `1009.5213` n `994`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1876`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1859`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
