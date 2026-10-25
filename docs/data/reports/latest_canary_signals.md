# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T20:07:27.072239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0718` n `13`; crypto_alt avg `-0.01` n `237`; crypto_major avg `-0.0429` n `8`; equity avg `-0.014` n `152`; fx avg `0.011` n `6`; index avg `-0.0077` n `26`; metal avg `-0.0074` n `20`; unknown avg `1.4896` n `1208`
- 1h: commodity avg `0.0579` n `13`; crypto_alt avg `-0.0365` n `237`; crypto_major avg `0.0352` n `8`; equity avg `-0.0199` n `152`; fx avg `0.0275` n `6`; index avg `-0.0069` n `26`; metal avg `-0.0101` n `20`; unknown avg `2.2995` n `1174`
- 4h: commodity avg `0.031` n `13`; crypto_alt avg `0.1564` n `237`; crypto_major avg `0.0767` n `8`; equity avg `0.1563` n `152`; fx avg `0.024` n `6`; index avg `0.0241` n `26`; metal avg `0.0344` n `20`; unknown avg `1.9077` n `1166`
- 24h: commodity avg `-0.1437` n `13`; crypto_alt avg `-0.0595` n `237`; crypto_major avg `0.4589` n `8`; equity avg `0.5603` n `152`; fx avg `0.0421` n `6`; index avg `0.1153` n `26`; metal avg `0.121` n `20`; unknown avg `9.7157` n `1029`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2265`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1686`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
