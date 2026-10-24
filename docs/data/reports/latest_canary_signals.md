# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T17:24:19.339348+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `13`; crypto_alt avg `0.1031` n `237`; crypto_major avg `0.0638` n `8`; equity avg `0.0373` n `152`; fx avg `0.0027` n `6`; index avg `0.005` n `26`; metal avg `0.0096` n `20`; unknown avg `0.0972` n `1231`
- 1h: commodity avg `-0.0034` n `13`; crypto_alt avg `0.8494` n `237`; crypto_major avg `0.7636` n `8`; equity avg `0.3271` n `152`; fx avg `-0.0009` n `6`; index avg `0.0405` n `26`; metal avg `0.0313` n `20`; unknown avg `1.3501` n `1207`
- 4h: commodity avg `-0.0367` n `13`; crypto_alt avg `-1.1537` n `237`; crypto_major avg `-0.8354` n `8`; equity avg `-0.2646` n `152`; fx avg `-0.0222` n `6`; index avg `-0.0456` n `26`; metal avg `-0.1095` n `20`; unknown avg `1.1083` n `1168`
- 24h: commodity avg `0.2356` n `13`; crypto_alt avg `-4.028` n `237`; crypto_major avg `-2.9613` n `8`; equity avg `-0.845` n `152`; fx avg `-0.0311` n `6`; index avg `-0.0678` n `26`; metal avg `-0.1902` n `20`; unknown avg `-0.5429` n `1045`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.185`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
