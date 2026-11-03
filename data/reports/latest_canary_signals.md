# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T07:07:28.911794+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1543` n `13`; crypto_alt avg `0.0743` n `239`; crypto_major avg `0.0622` n `8`; equity avg `-0.2276` n `157`; fx avg `0.0029` n `6`; index avg `-0.0374` n `27`; metal avg `-0.0465` n `20`; unknown avg `-0.0187` n `1254`
- 1h: commodity avg `0.3106` n `13`; crypto_alt avg `-0.2984` n `239`; crypto_major avg `0.0252` n `8`; equity avg `-0.1299` n `157`; fx avg `-0.0014` n `6`; index avg `-0.0387` n `27`; metal avg `-0.1059` n `20`; unknown avg `0.0665` n `1250`
- 4h: commodity avg `0.5103` n `13`; crypto_alt avg `-0.2734` n `239`; crypto_major avg `-0.1584` n `8`; equity avg `-1.0033` n `157`; fx avg `0.0444` n `6`; index avg `-0.1169` n `27`; metal avg `-0.3857` n `20`; unknown avg `0.0092` n `1164`
- 24h: commodity avg `-0.443` n `13`; crypto_alt avg `-2.8602` n `238`; crypto_major avg `-1.7794` n `8`; equity avg `-4.7233` n `157`; fx avg `-0.0142` n `6`; index avg `-0.3794` n `27`; metal avg `-0.4711` n `20`; unknown avg `8.2096` n `949`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
