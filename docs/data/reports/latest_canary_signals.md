# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T04:07:25.141869+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0093` n `13`; crypto_alt avg `-0.0514` n `237`; crypto_major avg `-0.0366` n `8`; equity avg `-0.5308` n `154`; fx avg `-0.0112` n `6`; index avg `-0.0022` n `27`; metal avg `0.0285` n `20`; unknown avg `0.1302` n `1228`
- 1h: commodity avg `0.0411` n `13`; crypto_alt avg `0.1179` n `237`; crypto_major avg `0.0937` n `8`; equity avg `-0.448` n `154`; fx avg `-0.0101` n `6`; index avg `0.0275` n `27`; metal avg `0.0736` n `20`; unknown avg `282.2506` n `1224`
- 4h: commodity avg `-0.0599` n `13`; crypto_alt avg `-1.06` n `237`; crypto_major avg `-0.6434` n `8`; equity avg `-1.0125` n `154`; fx avg `0.0059` n `6`; index avg `-0.0413` n `27`; metal avg `-0.0585` n `20`; unknown avg `283.2318` n `1218`
- 24h: commodity avg `0.0933` n `13`; crypto_alt avg `0.4272` n `237`; crypto_major avg `0.7756` n `8`; equity avg `1.2344` n `153`; fx avg `0.0033` n `6`; index avg `0.0876` n `27`; metal avg `-0.0612` n `20`; unknown avg `1011.552` n `994`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
