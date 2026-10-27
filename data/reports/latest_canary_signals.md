# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T04:37:32.998730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `13`; crypto_alt avg `-0.0365` n `237`; crypto_major avg `-0.1447` n `8`; equity avg `-0.0833` n `154`; fx avg `-0.0039` n `6`; index avg `-0.0014` n `27`; metal avg `-0.0527` n `20`; unknown avg `2.175` n `1236`
- 1h: commodity avg `-0.0373` n `13`; crypto_alt avg `-0.191` n `237`; crypto_major avg `-0.2864` n `8`; equity avg `-0.6455` n `154`; fx avg `-0.0248` n `6`; index avg `-0.0467` n `27`; metal avg `-0.0141` n `20`; unknown avg `77.5652` n `1226`
- 4h: commodity avg `-0.113` n `13`; crypto_alt avg `-1.0698` n `237`; crypto_major avg `-0.8579` n `8`; equity avg `-0.9914` n `154`; fx avg `-0.0082` n `6`; index avg `-0.0732` n `27`; metal avg `-0.0444` n `20`; unknown avg `151.9612` n `1218`
- 24h: commodity avg `0.06` n `13`; crypto_alt avg `-0.0688` n `237`; crypto_major avg `0.2384` n `8`; equity avg `0.953` n `153`; fx avg `-0.009` n `6`; index avg `0.0071` n `27`; metal avg `-0.125` n `20`; unknown avg `1110.7066` n `994`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1877`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
