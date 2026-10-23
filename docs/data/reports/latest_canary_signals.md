# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T00:22:41.374597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0317` n `13`; crypto_alt avg `0.1364` n `237`; crypto_major avg `-0.0055` n `8`; equity avg `0.1461` n `151`; fx avg `-0.0143` n `6`; index avg `0.0362` n `26`; metal avg `-0.0136` n `20`; unknown avg `0.4622` n `1233`
- 1h: commodity avg `-0.0451` n `13`; crypto_alt avg `0.2564` n `237`; crypto_major avg `0.079` n `8`; equity avg `-0.0717` n `151`; fx avg `-0.0447` n `6`; index avg `-0.0439` n `26`; metal avg `-0.0528` n `20`; unknown avg `0.1469` n `1225`
- 4h: commodity avg `-0.0353` n `13`; crypto_alt avg `0.053` n `237`; crypto_major avg `0.0456` n `8`; equity avg `-0.4974` n `151`; fx avg `-0.0545` n `6`; index avg `-0.0886` n `26`; metal avg `-0.0289` n `20`; unknown avg `0.3145` n `1167`
- 24h: commodity avg `0.4391` n `13`; crypto_alt avg `-4.7577` n `237`; crypto_major avg `-3.4774` n `8`; equity avg `-5.2049` n `151`; fx avg `-0.2128` n `6`; index avg `-0.6074` n `26`; metal avg `-1.0192` n `20`; unknown avg `54.488` n `905`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1815`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1715`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
