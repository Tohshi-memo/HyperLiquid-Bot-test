# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T11:22:28.394247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `13`; crypto_alt avg `-0.1491` n `236`; crypto_major avg `-0.1517` n `8`; equity avg `-0.056` n `151`; fx avg `-0.0059` n `6`; index avg `0.0183` n `26`; metal avg `-0.0043` n `20`; unknown avg `-0.0294` n `1193`
- 1h: commodity avg `-0.0029` n `13`; crypto_alt avg `-0.1193` n `236`; crypto_major avg `-0.0675` n `8`; equity avg `0.01` n `151`; fx avg `-0.007` n `6`; index avg `0.0199` n `26`; metal avg `0.0099` n `20`; unknown avg `0.3096` n `1191`
- 4h: commodity avg `0.0727` n `13`; crypto_alt avg `-0.396` n `236`; crypto_major avg `-0.2471` n `8`; equity avg `0.0642` n `151`; fx avg `-0.0002` n `6`; index avg `0.045` n `26`; metal avg `0.0026` n `20`; unknown avg `-0.0609` n `1173`
- 24h: commodity avg `0.3082` n `13`; crypto_alt avg `-2.68` n `236`; crypto_major avg `-2.1213` n `8`; equity avg `-3.4781` n `151`; fx avg `0.0019` n `6`; index avg `-0.5381` n `26`; metal avg `-0.2636` n `20`; unknown avg `9.1798` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1841`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1504`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1254`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0708`, n `666`, weak_sample_signal
