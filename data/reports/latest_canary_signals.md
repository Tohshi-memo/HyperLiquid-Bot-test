# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T23:07:33.951234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0308` n `13`; crypto_alt avg `0.0078` n `237`; crypto_major avg `-0.0876` n `8`; equity avg `-0.1528` n `151`; fx avg `-0.0058` n `6`; index avg `-0.0486` n `26`; metal avg `0.0158` n `20`; unknown avg `1.9611` n `1192`
- 1h: commodity avg `-0.0569` n `13`; crypto_alt avg `0.6942` n `237`; crypto_major avg `0.3619` n `8`; equity avg `0.3121` n `151`; fx avg `-0.0085` n `6`; index avg `-0.0004` n `26`; metal avg `0.0658` n `20`; unknown avg `2.9092` n `1184`
- 4h: commodity avg `-0.3102` n `13`; crypto_alt avg `0.9608` n `237`; crypto_major avg `1.135` n `8`; equity avg `1.1673` n `151`; fx avg `-0.0275` n `6`; index avg `0.2372` n `26`; metal avg `0.2034` n `20`; unknown avg `13.1964` n `1090`
- 24h: commodity avg `-0.2972` n `13`; crypto_alt avg `-1.7714` n `236`; crypto_major avg `0.4018` n `8`; equity avg `1.0227` n `151`; fx avg `-0.0221` n `6`; index avg `0.2218` n `26`; metal avg `0.2218` n `20`; unknown avg `2.4021` n `961`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2007`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1373`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1102`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0906`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0871`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0797`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0745`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
