# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T04:22:25.452408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0145` n `13`; crypto_alt avg `-0.0377` n `237`; crypto_major avg `-0.0255` n `8`; equity avg `-0.042` n `151`; fx avg `0.0007` n `6`; index avg `0.0002` n `26`; metal avg `-0.002` n `20`; unknown avg `-0.1035` n `1193`
- 1h: commodity avg `-0.021` n `13`; crypto_alt avg `0.1699` n `237`; crypto_major avg `0.132` n `8`; equity avg `0.0899` n `151`; fx avg `-0.0079` n `6`; index avg `0.0149` n `26`; metal avg `0.0103` n `20`; unknown avg `0.137` n `1185`
- 4h: commodity avg `0.0501` n `13`; crypto_alt avg `-0.0227` n `236`; crypto_major avg `0.6012` n `8`; equity avg `0.1544` n `151`; fx avg `-0.0196` n `6`; index avg `0.0388` n `26`; metal avg `0.0265` n `20`; unknown avg `0.2251` n `1185`
- 24h: commodity avg `-0.1299` n `13`; crypto_alt avg `-2.264` n `236`; crypto_major avg `-0.3274` n `8`; equity avg `-0.8114` n `151`; fx avg `-0.0467` n `6`; index avg `-0.0878` n `26`; metal avg `-0.0662` n `20`; unknown avg `3.7586` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1667`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1368`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1091`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0814`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
