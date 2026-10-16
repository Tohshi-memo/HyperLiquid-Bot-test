# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T20:07:31.314438+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0118` n `13`; crypto_alt avg `0.2079` n `236`; crypto_major avg `0.1132` n `8`; equity avg `0.1214` n `151`; fx avg `0.0075` n `6`; index avg `-0.0069` n `26`; metal avg `-0.0046` n `20`; unknown avg `0.7944` n `1149`
- 1h: commodity avg `-0.041` n `13`; crypto_alt avg `0.8764` n `236`; crypto_major avg `0.6979` n `8`; equity avg `0.3821` n `151`; fx avg `0.0155` n `6`; index avg `0.0544` n `26`; metal avg `0.0635` n `20`; unknown avg `157.5737` n `1149`
- 4h: commodity avg `0.4279` n `13`; crypto_alt avg `-0.6987` n `236`; crypto_major avg `-0.1244` n `8`; equity avg `-1.1558` n `151`; fx avg `0.0194` n `6`; index avg `-0.2525` n `26`; metal avg `-0.0479` n `20`; unknown avg `2.5052` n `1146`
- 24h: commodity avg `0.3049` n `13`; crypto_alt avg `-1.7608` n `236`; crypto_major avg `-1.753` n `8`; equity avg `-3.9813` n `151`; fx avg `0.0208` n `6`; index avg `-0.6737` n `26`; metal avg `-0.1174` n `20`; unknown avg `-0.2325` n `892`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1591`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1096`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1087`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0827`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0742`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0725`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
