# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T09:37:28.302066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `13`; crypto_alt avg `0.0356` n `237`; crypto_major avg `-0.0948` n `8`; equity avg `0.0025` n `152`; fx avg `0.0032` n `6`; index avg `0.0014` n `26`; metal avg `-0.0129` n `20`; unknown avg `-0.0727` n `1228`
- 1h: commodity avg `0.0107` n `13`; crypto_alt avg `-0.245` n `237`; crypto_major avg `-0.5691` n `8`; equity avg `-0.1326` n `152`; fx avg `0.0032` n `6`; index avg `-0.0164` n `26`; metal avg `-0.0321` n `20`; unknown avg `-0.2777` n `1214`
- 4h: commodity avg `0.2638` n `13`; crypto_alt avg `-0.905` n `237`; crypto_major avg `-1.0133` n `8`; equity avg `-0.32` n `152`; fx avg `0.0034` n `6`; index avg `-0.0366` n `26`; metal avg `-0.0349` n `20`; unknown avg `-0.2966` n `1178`
- 24h: commodity avg `0.1329` n `13`; crypto_alt avg `-2.6576` n `237`; crypto_major avg `-2.2276` n `8`; equity avg `-0.883` n `152`; fx avg `0.0146` n `6`; index avg `-0.0108` n `26`; metal avg `-0.1514` n `20`; unknown avg `193.5683` n `1053`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1667`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
