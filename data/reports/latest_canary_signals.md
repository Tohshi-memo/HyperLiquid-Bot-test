# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T19:52:28.800622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `13`; crypto_alt avg `-0.1065` n `235`; crypto_major avg `-0.0881` n `8`; equity avg `0.0093` n `144`; fx avg `-0.0071` n `6`; index avg `0.0009` n `26`; metal avg `0.0072` n `20`; unknown avg `2.3668` n `1078`
- 1h: commodity avg `-0.0037` n `13`; crypto_alt avg `0.1003` n `235`; crypto_major avg `0.0636` n `8`; equity avg `0.0105` n `144`; fx avg `-0.006` n `6`; index avg `-0.0031` n `26`; metal avg `0.0155` n `20`; unknown avg `2.6306` n `1076`
- 4h: commodity avg `0.0364` n `13`; crypto_alt avg `0.391` n `235`; crypto_major avg `0.2378` n `8`; equity avg `0.039` n `144`; fx avg `-0.0169` n `6`; index avg `0.0023` n `26`; metal avg `0.0237` n `20`; unknown avg `0.4785` n `1068`
- 24h: commodity avg `0.0349` n `13`; crypto_alt avg `1.104` n `235`; crypto_major avg `1.0168` n `8`; equity avg `0.1848` n `144`; fx avg `0.0148` n `6`; index avg `-0.0226` n `26`; metal avg `0.0151` n `20`; unknown avg `0.3394` n `1024`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1821`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
