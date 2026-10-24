# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T19:52:24.523198+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `13`; crypto_alt avg `-0.0589` n `237`; crypto_major avg `-0.0707` n `8`; equity avg `-0.0182` n `152`; fx avg `0.0063` n `6`; index avg `-0.0006` n `26`; metal avg `-0.001` n `20`; unknown avg `0.0231` n `1231`
- 1h: commodity avg `-0.0248` n `13`; crypto_alt avg `-0.0953` n `237`; crypto_major avg `0.0983` n `8`; equity avg `0.1011` n `152`; fx avg `-0.0158` n `6`; index avg `0.0279` n `26`; metal avg `0.0237` n `20`; unknown avg `4.8161` n `1211`
- 4h: commodity avg `-0.0541` n `13`; crypto_alt avg `1.362` n `237`; crypto_major avg `1.3868` n `8`; equity avg `0.5724` n `152`; fx avg `-0.0104` n `6`; index avg `0.0758` n `26`; metal avg `0.0632` n `20`; unknown avg `2.3868` n `1181`
- 24h: commodity avg `0.0607` n `13`; crypto_alt avg `-2.5783` n `237`; crypto_major avg `-1.5732` n `8`; equity avg `-0.1006` n `152`; fx avg `-0.0503` n `6`; index avg `-0.0158` n `26`; metal avg `-0.1668` n `20`; unknown avg `108.3276` n `1030`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1918`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1821`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
