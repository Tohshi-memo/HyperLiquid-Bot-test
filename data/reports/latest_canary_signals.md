# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T07:22:31.156453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `13`; crypto_alt avg `-0.0923` n `237`; crypto_major avg `-0.0414` n `8`; equity avg `-0.0214` n `151`; fx avg `0.0009` n `6`; index avg `-0.0022` n `26`; metal avg `0.0004` n `20`; unknown avg `0.0168` n `1193`
- 1h: commodity avg `0.0035` n `13`; crypto_alt avg `0.115` n `237`; crypto_major avg `0.0705` n `8`; equity avg `0.1035` n `151`; fx avg `-0.0079` n `6`; index avg `0.0288` n `26`; metal avg `0.0042` n `20`; unknown avg `0.0362` n `1191`
- 4h: commodity avg `-0.0445` n `13`; crypto_alt avg `-0.4877` n `237`; crypto_major avg `-0.2642` n `8`; equity avg `0.1714` n `151`; fx avg `-0.013` n `6`; index avg `0.0478` n `26`; metal avg `0.0045` n `20`; unknown avg `0.2655` n `1169`
- 24h: commodity avg `0.1035` n `13`; crypto_alt avg `-2.6359` n `236`; crypto_major avg `-0.9112` n `8`; equity avg `-0.7996` n `151`; fx avg `-0.0529` n `6`; index avg `-0.0785` n `26`; metal avg `-0.0597` n `20`; unknown avg `3.9957` n `1053`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1703`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1321`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1084`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0835`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
