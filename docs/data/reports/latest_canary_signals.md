# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T05:49:38.748421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `13`; crypto_alt avg `0.0079` n `237`; crypto_major avg `-0.0043` n `8`; equity avg `0.0443` n `151`; fx avg `-0.0064` n `6`; index avg `0.0158` n `26`; metal avg `0.0025` n `20`; unknown avg `0.2446` n `1193`
- 1h: commodity avg `-0.0244` n `13`; crypto_alt avg `-0.7115` n `237`; crypto_major avg `-0.3451` n `8`; equity avg `-0.0538` n `151`; fx avg `0.0072` n `6`; index avg `-0.0031` n `26`; metal avg `-0.0032` n `20`; unknown avg `-0.0744` n `1191`
- 4h: commodity avg `-0.0223` n `13`; crypto_alt avg `-1.0272` n `237`; crypto_major avg `-0.2895` n `8`; equity avg `-0.0219` n `151`; fx avg `-0.0104` n `6`; index avg `0.0064` n `26`; metal avg `0.0083` n `20`; unknown avg `-0.2014` n `1185`
- 24h: commodity avg `-0.1357` n `13`; crypto_alt avg `-3.0967` n `236`; crypto_major avg `-0.913` n `8`; equity avg `-0.8984` n `151`; fx avg `-0.0394` n `6`; index avg `-0.114` n `26`; metal avg `-0.0499` n `20`; unknown avg `4.0395` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1689`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1323`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.107`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0787`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
