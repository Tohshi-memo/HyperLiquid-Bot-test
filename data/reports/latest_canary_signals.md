# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T19:07:28.096831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0213` n `12`; crypto_alt avg `0.0743` n `233`; crypto_major avg `0.114` n `8`; equity avg `0.0283` n `136`; fx avg `0.0023` n `6`; index avg `0.0038` n `27`; metal avg `0.0029` n `20`; unknown avg `0.0909` n `838`
- 1h: commodity avg `0.0158` n `12`; crypto_alt avg `0.16` n `233`; crypto_major avg `0.2242` n `8`; equity avg `0.0593` n `136`; fx avg `0.0072` n `6`; index avg `-0.0003` n `27`; metal avg `0.0129` n `20`; unknown avg `-0.351` n `830`
- 4h: commodity avg `0.035` n `12`; crypto_alt avg `0.5438` n `233`; crypto_major avg `0.6951` n `8`; equity avg `0.3317` n `136`; fx avg `0.0077` n `6`; index avg `-0.0045` n `27`; metal avg `0.0241` n `20`; unknown avg `80.8503` n `766`
- 24h: commodity avg `0.2702` n `12`; crypto_alt avg `0.3016` n `233`; crypto_major avg `-0.4639` n `8`; equity avg `-1.3276` n `136`; fx avg `0.0062` n `6`; index avg `-0.2625` n `26`; metal avg `-0.0665` n `20`; unknown avg `1.1676` n `720`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
