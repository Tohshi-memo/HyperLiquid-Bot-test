# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T21:52:30.985337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0056` n `13`; crypto_alt avg `-0.008` n `237`; crypto_major avg `-0.0039` n `8`; equity avg `-0.1126` n `151`; fx avg `-0.0006` n `6`; index avg `-0.0057` n `26`; metal avg `-0.001` n `20`; unknown avg `-0.1518` n `1233`
- 1h: commodity avg `-0.0406` n `13`; crypto_alt avg `0.3913` n `237`; crypto_major avg `0.3862` n `8`; equity avg `0.088` n `151`; fx avg `0.0042` n `6`; index avg `-0.0103` n `26`; metal avg `0.0451` n `20`; unknown avg `6.7761` n `1225`
- 4h: commodity avg `-0.1778` n `13`; crypto_alt avg `-0.1469` n `237`; crypto_major avg `0.1647` n `8`; equity avg `-0.3416` n `151`; fx avg `-0.041` n `6`; index avg `-0.0738` n `26`; metal avg `-0.0967` n `20`; unknown avg `-0.6268` n `1167`
- 24h: commodity avg `0.5111` n `13`; crypto_alt avg `-5.319` n `237`; crypto_major avg `-3.8827` n `8`; equity avg `-5.9498` n `151`; fx avg `-0.1836` n `6`; index avg `-0.7394` n `26`; metal avg `-0.9654` n `20`; unknown avg `60.2142` n `934`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
