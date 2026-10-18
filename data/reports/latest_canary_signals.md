# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T02:07:24.035553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `13`; crypto_alt avg `-0.2775` n `237`; crypto_major avg `-0.1324` n `8`; equity avg `-0.1509` n `151`; fx avg `0.0024` n `6`; index avg `-0.0333` n `26`; metal avg `0.0004` n `20`; unknown avg `-0.22` n `1191`
- 1h: commodity avg `0.0687` n `13`; crypto_alt avg `-0.435` n `237`; crypto_major avg `-0.1083` n `8`; equity avg `-0.2012` n `151`; fx avg `-0.0015` n `6`; index avg `-0.0312` n `26`; metal avg `-0.0046` n `20`; unknown avg `-0.222` n `1191`
- 4h: commodity avg `-0.0079` n `13`; crypto_alt avg `0.2843` n `236`; crypto_major avg `0.6626` n `8`; equity avg `0.2115` n `151`; fx avg `0.0084` n `6`; index avg `0.0344` n `26`; metal avg `0.0473` n `20`; unknown avg `0.364` n `1185`
- 24h: commodity avg `-0.103` n `13`; crypto_alt avg `-2.3364` n `236`; crypto_major avg `-0.6444` n `8`; equity avg `-0.9827` n `151`; fx avg `-0.0151` n `6`; index avg `-0.1053` n `26`; metal avg `-0.0418` n `20`; unknown avg `3.6958` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1622`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1331`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.102`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0752`, n `666`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
