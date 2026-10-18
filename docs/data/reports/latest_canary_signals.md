# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T15:07:28.041680+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1922` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0157` n `13`; crypto_alt avg `0.2407` n `237`; crypto_major avg `0.2004` n `8`; equity avg `0.0573` n `151`; fx avg `0.0012` n `6`; index avg `0.0061` n `26`; metal avg `0.0108` n `20`; unknown avg `-0.3006` n `1191`
- 1h: commodity avg `-0.017` n `13`; crypto_alt avg `0.1491` n `237`; crypto_major avg `-0.0446` n `8`; equity avg `-0.0042` n `151`; fx avg `-0.0001` n `6`; index avg `-0.007` n `26`; metal avg `0.0012` n `20`; unknown avg `-0.1751` n `1191`
- 4h: commodity avg `0.0643` n `13`; crypto_alt avg `-1.0425` n `237`; crypto_major avg `-1.2911` n `8`; equity avg `-0.48` n `151`; fx avg `0.0119` n `6`; index avg `-0.0989` n `26`; metal avg `-0.0316` n `20`; unknown avg `-0.0406` n `1183`
- 24h: commodity avg `0.0259` n `13`; crypto_alt avg `-2.9466` n `236`; crypto_major avg `-1.2869` n `8`; equity avg `-0.9206` n `151`; fx avg `-0.0307` n `6`; index avg `-0.1332` n `26`; metal avg `-0.0573` n `20`; unknown avg `0.6796` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2096`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1394`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1291`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1092`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0796`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
