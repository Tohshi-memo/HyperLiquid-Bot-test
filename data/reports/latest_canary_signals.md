# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T21:22:30.642181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `13`; crypto_alt avg `-0.0776` n `237`; crypto_major avg `0.0473` n `8`; equity avg `-0.0342` n `152`; fx avg `-0.0065` n `6`; index avg `-0.0059` n `26`; metal avg `-0.0076` n `20`; unknown avg `0.6016` n `1231`
- 1h: commodity avg `-0.0388` n `13`; crypto_alt avg `-0.2676` n `237`; crypto_major avg `-0.1483` n `8`; equity avg `-0.1248` n `152`; fx avg `0.0014` n `6`; index avg `-0.0115` n `26`; metal avg `-0.0213` n `20`; unknown avg `0.824` n `1223`
- 4h: commodity avg `-0.0214` n `13`; crypto_alt avg `0.586` n `237`; crypto_major avg `0.7031` n `8`; equity avg `0.1773` n `152`; fx avg `-0.003` n `6`; index avg `0.0283` n `26`; metal avg `0.0154` n `20`; unknown avg `0.8331` n `1175`
- 24h: commodity avg `0.0653` n `13`; crypto_alt avg `-2.5038` n `237`; crypto_major avg `-1.7242` n `8`; equity avg `-0.3463` n `152`; fx avg `-0.0374` n `6`; index avg `-0.0602` n `26`; metal avg `-0.1654` n `20`; unknown avg `0.9644` n `1076`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1803`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
