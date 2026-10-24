# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T09:52:27.797724+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0233` n `13`; crypto_alt avg `0.0746` n `237`; crypto_major avg `0.0917` n `8`; equity avg `0.0032` n `152`; fx avg `0.0001` n `6`; index avg `-0.0041` n `26`; metal avg `0.0064` n `20`; unknown avg `0.1321` n `1230`
- 1h: commodity avg `0.0319` n `13`; crypto_alt avg `0.0698` n `237`; crypto_major avg `-0.2365` n `8`; equity avg `-0.0829` n `152`; fx avg `0.0021` n `6`; index avg `-0.0131` n `26`; metal avg `-0.0231` n `20`; unknown avg `12.079` n `1214`
- 4h: commodity avg `0.0586` n `13`; crypto_alt avg `-0.812` n `237`; crypto_major avg `-0.9273` n `8`; equity avg `-0.3337` n `152`; fx avg `0.0005` n `6`; index avg `-0.0417` n `26`; metal avg `-0.0297` n `20`; unknown avg `13.2125` n `1180`
- 24h: commodity avg `0.1573` n `13`; crypto_alt avg `-2.5986` n `237`; crypto_major avg `-2.2424` n `8`; equity avg `-0.8878` n `152`; fx avg `0.006` n `6`; index avg `-0.0142` n `26`; metal avg `-0.1447` n `20`; unknown avg `193.5747` n `1053`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
