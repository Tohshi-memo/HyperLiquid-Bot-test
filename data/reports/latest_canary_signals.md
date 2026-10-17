# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T18:07:29.018992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0044` n `13`; crypto_alt avg `0.3497` n `236`; crypto_major avg `0.1699` n `8`; equity avg `0.1198` n `151`; fx avg `-0.012` n `6`; index avg `0.0014` n `26`; metal avg `0.0045` n `20`; unknown avg `-0.4566` n `1191`
- 1h: commodity avg `0.0297` n `13`; crypto_alt avg `0.7234` n `236`; crypto_major avg `0.4842` n `8`; equity avg `0.1191` n `151`; fx avg `-0.019` n `6`; index avg `0.0049` n `26`; metal avg `0.0079` n `20`; unknown avg `0.1097` n `1191`
- 4h: commodity avg `-0.0977` n `13`; crypto_alt avg `-0.3854` n `236`; crypto_major avg `-0.1847` n `8`; equity avg `-0.1828` n `151`; fx avg `-0.0346` n `6`; index avg `-0.0546` n `26`; metal avg `-0.0421` n `20`; unknown avg `2.1798` n `1135`
- 24h: commodity avg `0.0666` n `13`; crypto_alt avg `-1.2985` n `236`; crypto_major avg `-0.2879` n `8`; equity avg `-0.6818` n `151`; fx avg `-0.0183` n `6`; index avg `-0.1233` n `26`; metal avg `-0.0334` n `20`; unknown avg `3.753` n `1027`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.171`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1479`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1139`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1132`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0722`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
