# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T09:22:31.736742+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0292` n `13`; crypto_alt avg `0.128` n `237`; crypto_major avg `0.1659` n `8`; equity avg `0.073` n `151`; fx avg `-0.0141` n `6`; index avg `0.0091` n `26`; metal avg `0.005` n `20`; unknown avg `0.0279` n `1195`
- 1h: commodity avg `0.2412` n `13`; crypto_alt avg `-0.0801` n `237`; crypto_major avg `0.1238` n `8`; equity avg `-0.0351` n `151`; fx avg `0.0225` n `6`; index avg `-0.0057` n `26`; metal avg `0.0118` n `20`; unknown avg `0.1314` n `1193`
- 4h: commodity avg `0.1737` n `13`; crypto_alt avg `0.3784` n `237`; crypto_major avg `0.3008` n `8`; equity avg `0.0151` n `151`; fx avg `-0.0173` n `6`; index avg `-0.0121` n `26`; metal avg `-0.055` n `20`; unknown avg `0.4573` n `1126`
- 24h: commodity avg `-0.2417` n `13`; crypto_alt avg `0.3633` n `237`; crypto_major avg `1.1504` n `8`; equity avg `2.3336` n `151`; fx avg `-0.0517` n `6`; index avg `0.4315` n `26`; metal avg `0.2349` n `20`; unknown avg `1.2191` n `971`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1985`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1442`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1272`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1072`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0613`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
