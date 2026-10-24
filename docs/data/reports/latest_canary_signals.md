# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T17:07:27.806033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0187` n `13`; crypto_alt avg `-0.0689` n `237`; crypto_major avg `-0.0798` n `8`; equity avg `-0.0113` n `152`; fx avg `-0.0052` n `6`; index avg `0.0008` n `26`; metal avg `-0.008` n `20`; unknown avg `-0.0528` n `1213`
- 1h: commodity avg `-0.0015` n `13`; crypto_alt avg `0.5546` n `237`; crypto_major avg `0.5172` n `8`; equity avg `0.282` n `152`; fx avg `-0.0078` n `6`; index avg `0.0337` n `26`; metal avg `0.0196` n `20`; unknown avg `0.9053` n `1207`
- 4h: commodity avg `-0.0158` n `13`; crypto_alt avg `-1.4247` n `237`; crypto_major avg `-1.0258` n `8`; equity avg `-0.3567` n `152`; fx avg `-0.0285` n `6`; index avg `-0.055` n `26`; metal avg `-0.1215` n `20`; unknown avg `0.9932` n `1166`
- 24h: commodity avg `0.2355` n `13`; crypto_alt avg `-4.0557` n `237`; crypto_major avg `-3.0584` n `8`; equity avg `-0.979` n `152`; fx avg `-0.0402` n `6`; index avg `-0.1001` n `26`; metal avg `-0.247` n `20`; unknown avg `-0.7638` n `1045`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1913`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
