# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T06:52:28.738019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `13`; crypto_alt avg `-0.0719` n `237`; crypto_major avg `-0.1007` n `8`; equity avg `-0.0123` n `151`; fx avg `-0.0044` n `6`; index avg `0.005` n `26`; metal avg `-0.0014` n `20`; unknown avg `-0.0345` n `1193`
- 1h: commodity avg `-0.0062` n `13`; crypto_alt avg `0.4786` n `237`; crypto_major avg `0.1693` n `8`; equity avg `0.1229` n `151`; fx avg `-0.0069` n `6`; index avg `0.0183` n `26`; metal avg `-0.0032` n `20`; unknown avg `0.1279` n `1175`
- 4h: commodity avg `-0.0522` n `13`; crypto_alt avg `-0.1871` n `237`; crypto_major avg `-0.1429` n `8`; equity avg `0.2091` n `151`; fx avg `-0.0139` n `6`; index avg `0.0412` n `26`; metal avg `0.0027` n `20`; unknown avg `0.1859` n `1169`
- 24h: commodity avg `0.0499` n `13`; crypto_alt avg `-2.6247` n `236`; crypto_major avg `-0.8434` n `8`; equity avg `-0.8538` n `151`; fx avg `-0.0484` n `6`; index avg `-0.0992` n `26`; metal avg `-0.0694` n `20`; unknown avg `3.9021` n `1053`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1684`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1324`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1083`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0817`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
