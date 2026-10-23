# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T05:22:27.239413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `13`; crypto_alt avg `0.1264` n `237`; crypto_major avg `0.08` n `8`; equity avg `0.121` n `151`; fx avg `-0.0132` n `6`; index avg `-0.0041` n `26`; metal avg `0.0412` n `20`; unknown avg `0.1366` n `1233`
- 1h: commodity avg `0.0514` n `13`; crypto_alt avg `0.2174` n `237`; crypto_major avg `0.1358` n `8`; equity avg `0.4518` n `151`; fx avg `0.008` n `6`; index avg `0.0192` n `26`; metal avg `0.0974` n `20`; unknown avg `0.0777` n `1229`
- 4h: commodity avg `0.0367` n `13`; crypto_alt avg `1.1597` n `237`; crypto_major avg `0.605` n `8`; equity avg `0.9618` n `151`; fx avg `0.0559` n `6`; index avg `0.0761` n `26`; metal avg `0.0381` n `20`; unknown avg `-0.1447` n `1221`
- 24h: commodity avg `0.262` n `13`; crypto_alt avg `-1.2115` n `237`; crypto_major avg `-0.839` n `8`; equity avg `-2.0677` n `151`; fx avg `-0.1231` n `6`; index avg `-0.1915` n `26`; metal avg `-0.4815` n `20`; unknown avg `52.8564` n `901`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.186`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1726`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
