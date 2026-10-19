# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T00:22:28.335950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9714` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2165` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0131` n `13`; crypto_alt avg `-0.1347` n `237`; crypto_major avg `-0.1024` n `8`; equity avg `-0.0766` n `151`; fx avg `-0.0106` n `6`; index avg `-0.0401` n `26`; metal avg `-0.0504` n `20`; unknown avg `-0.0631` n `1194`
- 1h: commodity avg `-0.1155` n `13`; crypto_alt avg `0.4016` n `237`; crypto_major avg `0.3026` n `8`; equity avg `0.7716` n `151`; fx avg `0.0215` n `6`; index avg `0.165` n `26`; metal avg `0.0091` n `20`; unknown avg `3.1845` n `1184`
- 4h: commodity avg `-0.4741` n `13`; crypto_alt avg `3.0472` n `237`; crypto_major avg `2.4973` n `8`; equity avg `2.2932` n `151`; fx avg `0.0411` n `6`; index avg `0.4423` n `26`; metal avg `0.2808` n `20`; unknown avg `5.4591` n `1096`
- 24h: commodity avg `-0.3708` n `13`; crypto_alt avg `-1.4517` n `236`; crypto_major avg `0.55` n `8`; equity avg `1.854` n `151`; fx avg `-0.0072` n `6`; index avg `0.379` n `26`; metal avg `0.2229` n `20`; unknown avg `2.1212` n `959`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2002`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1359`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0891`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0773`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0732`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0634`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
