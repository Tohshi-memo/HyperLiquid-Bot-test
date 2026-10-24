# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T21:07:33.545970+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `13`; crypto_alt avg `-0.3193` n `237`; crypto_major avg `-0.2594` n `8`; equity avg `-0.0949` n `152`; fx avg `0.0103` n `6`; index avg `-0.0052` n `26`; metal avg `-0.0103` n `20`; unknown avg `0.0822` n `1223`
- 1h: commodity avg `0.0019` n `13`; crypto_alt avg `-0.1103` n `237`; crypto_major avg `-0.1791` n `8`; equity avg `-0.0843` n `152`; fx avg `0.005` n `6`; index avg `-0.0059` n `26`; metal avg `-0.0154` n `20`; unknown avg `-0.082` n `1221`
- 4h: commodity avg `-0.0253` n `13`; crypto_alt avg `0.7698` n `237`; crypto_major avg `0.7197` n `8`; equity avg `0.249` n `152`; fx avg `0.0061` n `6`; index avg `0.0393` n `26`; metal avg `0.0325` n `20`; unknown avg `0.7303` n `1175`
- 24h: commodity avg `0.0721` n `13`; crypto_alt avg `-2.5122` n `237`; crypto_major avg `-1.7879` n `8`; equity avg `-0.3561` n `152`; fx avg `-0.0163` n `6`; index avg `-0.0571` n `26`; metal avg `-0.1552` n `20`; unknown avg `0.2712` n `1076`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1918`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
