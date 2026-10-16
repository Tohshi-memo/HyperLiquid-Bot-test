# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T12:37:27.399946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1244` n `13`; crypto_alt avg `0.0577` n `236`; crypto_major avg `-0.0474` n `8`; equity avg `-0.1` n `151`; fx avg `-0.0078` n `6`; index avg `-0.0093` n `26`; metal avg `-0.0085` n `20`; unknown avg `0.4974` n `1136`
- 1h: commodity avg `-0.2601` n `13`; crypto_alt avg `-0.131` n `236`; crypto_major avg `-0.509` n `8`; equity avg `-0.1126` n `151`; fx avg `-0.0248` n `6`; index avg `0.0203` n `26`; metal avg `-0.0322` n `20`; unknown avg `1.0308` n `1128`
- 4h: commodity avg `-0.0856` n `13`; crypto_alt avg `0.2507` n `236`; crypto_major avg `-0.0204` n `8`; equity avg `-0.6096` n `151`; fx avg `0.0298` n `6`; index avg `-0.0264` n `26`; metal avg `-0.0503` n `20`; unknown avg `1.9425` n `1128`
- 24h: commodity avg `-0.0201` n `13`; crypto_alt avg `5.1203` n `236`; crypto_major avg `2.7497` n `8`; equity avg `2.4794` n `151`; fx avg `0.0008` n `6`; index avg `0.3383` n `26`; metal avg `0.2435` n `20`; unknown avg `25.2218` n `944`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0973`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0908`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0858`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0835`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0742`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
