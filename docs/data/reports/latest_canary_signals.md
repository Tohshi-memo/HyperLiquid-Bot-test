# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T01:07:25.797467+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `13`; crypto_alt avg `0.334` n `237`; crypto_major avg `0.2348` n `8`; equity avg `0.1168` n `151`; fx avg `0.003` n `6`; index avg `0.0103` n `26`; metal avg `0.0057` n `20`; unknown avg `0.3486` n `1191`
- 1h: commodity avg `-0.0315` n `13`; crypto_alt avg `0.2912` n `236`; crypto_major avg `0.4559` n `8`; equity avg `0.2106` n `151`; fx avg `0.0017` n `6`; index avg `0.0397` n `26`; metal avg `0.0242` n `20`; unknown avg `0.4325` n `1191`
- 4h: commodity avg `-0.0618` n `13`; crypto_alt avg `-0.7496` n `236`; crypto_major avg `-0.3655` n `8`; equity avg `-0.5819` n `151`; fx avg `0.0075` n `6`; index avg `-0.0588` n `26`; metal avg `-0.0228` n `20`; unknown avg `0.1424` n `1185`
- 24h: commodity avg `-0.1456` n `13`; crypto_alt avg `-1.9103` n `236`; crypto_major avg `-0.465` n `8`; equity avg `-0.8042` n `151`; fx avg `-0.0238` n `6`; index avg `-0.084` n `26`; metal avg `-0.0512` n `20`; unknown avg `3.8748` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1627`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.132`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1006`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0733`, n `666`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
