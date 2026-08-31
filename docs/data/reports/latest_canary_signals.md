# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T07:52:25.597803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0569` n `12`; crypto_alt avg `-0.0075` n `232`; crypto_major avg `0.0302` n `8`; equity avg `-0.0736` n `128`; fx avg `0.0105` n `6`; index avg `0.0003` n `26`; metal avg `-0.0341` n `20`; unknown avg `0.1358` n `793`
- 1h: commodity avg `-0.0875` n `12`; crypto_alt avg `0.1922` n `232`; crypto_major avg `0.1354` n `8`; equity avg `-0.0989` n `128`; fx avg `-0.0045` n `6`; index avg `-0.0047` n `26`; metal avg `-0.0154` n `20`; unknown avg `0.0395` n `791`
- 4h: commodity avg `-0.081` n `12`; crypto_alt avg `0.6322` n `232`; crypto_major avg `0.6019` n `8`; equity avg `1.0059` n `128`; fx avg `-0.038` n `6`; index avg `0.1959` n `26`; metal avg `0.1739` n `20`; unknown avg `0.2598` n `773`
- 24h: commodity avg `0.3122` n `12`; crypto_alt avg `0.408` n `231`; crypto_major avg `-1.1637` n `8`; equity avg `-0.1845` n `128`; fx avg `-0.1025` n `6`; index avg `-0.0324` n `26`; metal avg `-0.2171` n `20`; unknown avg `-0.459` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
