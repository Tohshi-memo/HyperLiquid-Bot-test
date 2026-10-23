# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T04:07:29.855322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `13`; crypto_alt avg `-0.0907` n `237`; crypto_major avg `-0.1926` n `8`; equity avg `0.1193` n `151`; fx avg `0.0118` n `6`; index avg `0.0156` n `26`; metal avg `-0.0555` n `20`; unknown avg `-0.2247` n `1225`
- 1h: commodity avg `-0.0329` n `13`; crypto_alt avg `0.1443` n `237`; crypto_major avg `-0.046` n `8`; equity avg `0.4913` n `151`; fx avg `-0.0057` n `6`; index avg `0.0941` n `26`; metal avg `-0.0347` n `20`; unknown avg `0.5598` n `1225`
- 4h: commodity avg `0.0796` n `13`; crypto_alt avg `1.3852` n `237`; crypto_major avg `0.7782` n `8`; equity avg `1.5678` n `151`; fx avg `0.0198` n `6`; index avg `0.1949` n `26`; metal avg `-0.0586` n `20`; unknown avg `0.8418` n `1223`
- 24h: commodity avg `0.3951` n `13`; crypto_alt avg `-1.7144` n `237`; crypto_major avg `-1.0308` n `8`; equity avg `-2.4981` n `151`; fx avg `-0.1203` n `6`; index avg `-0.2463` n `26`; metal avg `-0.5771` n `20`; unknown avg `59.7429` n `903`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1617`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
