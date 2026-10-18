# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T01:52:26.273367+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.071` n `13`; crypto_alt avg `0.0437` n `237`; crypto_major avg `0.0586` n `8`; equity avg `-0.0238` n `151`; fx avg `-0.0001` n `6`; index avg `0.008` n `26`; metal avg `0.0049` n `20`; unknown avg `0.2966` n `1193`
- 1h: commodity avg `0.0619` n `13`; crypto_alt avg `0.1749` n `237`; crypto_major avg `0.2587` n `8`; equity avg `0.0659` n `151`; fx avg `-0.0009` n `6`; index avg `0.0124` n `26`; metal avg `0.0007` n `20`; unknown avg `0.4903` n `1191`
- 4h: commodity avg `-0.0329` n `13`; crypto_alt avg `0.8349` n `236`; crypto_major avg `0.9497` n `8`; equity avg `0.4221` n `151`; fx avg `0.0053` n `6`; index avg `0.082` n `26`; metal avg `0.0618` n `20`; unknown avg `0.8895` n `1185`
- 24h: commodity avg `-0.105` n `13`; crypto_alt avg `-1.8143` n `236`; crypto_major avg `-0.4096` n `8`; equity avg `-0.7646` n `151`; fx avg `-0.041` n `6`; index avg `-0.0689` n `26`; metal avg `-0.0524` n `20`; unknown avg `3.6809` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1626`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1324`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0748`, n `666`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
