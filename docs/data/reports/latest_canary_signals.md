# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T17:37:31.606884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.119` n `12`; crypto_alt avg `-0.2711` n `234`; crypto_major avg `-0.2489` n `8`; equity avg `-0.1125` n `141`; fx avg `-0.0068` n `6`; index avg `-0.013` n `26`; metal avg `-0.0486` n `20`; unknown avg `0.2181` n `960`
- 1h: commodity avg `0.0246` n `12`; crypto_alt avg `-0.4806` n `234`; crypto_major avg `-0.492` n `8`; equity avg `-0.182` n `141`; fx avg `-0.0091` n `6`; index avg `-0.0239` n `26`; metal avg `-0.0479` n `20`; unknown avg `-0.3305` n `958`
- 4h: commodity avg `-0.1808` n `12`; crypto_alt avg `-0.3129` n `234`; crypto_major avg `-0.7567` n `8`; equity avg `-0.338` n `141`; fx avg `-0.0007` n `6`; index avg `0.0342` n `26`; metal avg `0.0703` n `20`; unknown avg `4.3509` n `894`
- 24h: commodity avg `-0.8789` n `12`; crypto_alt avg `1.4235` n `234`; crypto_major avg `0.2896` n `8`; equity avg `0.1486` n `141`; fx avg `-0.252` n `6`; index avg `0.1932` n `26`; metal avg `0.1755` n `20`; unknown avg `1601.7239` n `805`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1773`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
