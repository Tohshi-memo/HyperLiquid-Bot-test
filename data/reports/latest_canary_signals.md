# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T21:22:32.042239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0171` n `13`; crypto_alt avg `0.3561` n `237`; crypto_major avg `0.3503` n `8`; equity avg `0.1845` n `151`; fx avg `0.0089` n `6`; index avg `0.0123` n `26`; metal avg `0.0079` n `20`; unknown avg `0.9978` n `1233`
- 1h: commodity avg `-0.0373` n `13`; crypto_alt avg `0.3416` n `237`; crypto_major avg `0.3865` n `8`; equity avg `-0.0596` n `151`; fx avg `-0.0052` n `6`; index avg `-0.0301` n `26`; metal avg `0.0275` n `20`; unknown avg `1.1975` n `1213`
- 4h: commodity avg `0.0512` n `13`; crypto_alt avg `0.0309` n `237`; crypto_major avg `0.3259` n `8`; equity avg `-0.2849` n `151`; fx avg `-0.0463` n `6`; index avg `-0.0741` n `26`; metal avg `-0.1348` n `20`; unknown avg `-0.239` n `1167`
- 24h: commodity avg `0.5168` n `13`; crypto_alt avg `-5.0856` n `237`; crypto_major avg `-3.6459` n `8`; equity avg `-5.7173` n `151`; fx avg `-0.1875` n `6`; index avg `-0.7059` n `26`; metal avg `-0.9734` n `20`; unknown avg `60.1855` n `934`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
