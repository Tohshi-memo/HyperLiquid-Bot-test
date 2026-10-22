# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T23:37:32.251043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0593` n `13`; crypto_alt avg `-0.0009` n `237`; crypto_major avg `-0.0186` n `8`; equity avg `-0.2019` n `151`; fx avg `0.0016` n `6`; index avg `-0.0334` n `26`; metal avg `-0.0299` n `20`; unknown avg `-0.0521` n `1233`
- 1h: commodity avg `0.0952` n `13`; crypto_alt avg `-0.2317` n `237`; crypto_major avg `-0.1762` n `8`; equity avg `-0.4276` n `151`; fx avg `0.0141` n `6`; index avg `-0.0636` n `26`; metal avg `-0.0296` n `20`; unknown avg `0.1134` n `1231`
- 4h: commodity avg `0.0397` n `13`; crypto_alt avg `-0.3696` n `237`; crypto_major avg `-0.238` n `8`; equity avg `-0.3614` n `151`; fx avg `-0.0218` n `6`; index avg `-0.023` n `26`; metal avg `0.0035` n `20`; unknown avg `0.0463` n `1127`
- 24h: commodity avg `0.545` n `13`; crypto_alt avg `-4.9967` n `237`; crypto_major avg `-3.5703` n `8`; equity avg `-5.3232` n `151`; fx avg `-0.1669` n `6`; index avg `-0.5974` n `26`; metal avg `-0.9971` n `20`; unknown avg `54.455` n `905`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
