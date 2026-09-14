# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T23:37:28.155337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0162` n `12`; crypto_alt avg `-0.0802` n `233`; crypto_major avg `-0.1932` n `8`; equity avg `0.0194` n `136`; fx avg `0.0197` n `6`; index avg `0.0004` n `27`; metal avg `-0.0092` n `20`; unknown avg `0.7875` n `908`
- 1h: commodity avg `0.0323` n `12`; crypto_alt avg `-0.2861` n `233`; crypto_major avg `-0.5842` n `8`; equity avg `0.0535` n `136`; fx avg `0.0027` n `6`; index avg `0.014` n `27`; metal avg `-0.0596` n `20`; unknown avg `0.5355` n `906`
- 4h: commodity avg `0.1171` n `12`; crypto_alt avg `-0.6824` n `233`; crypto_major avg `-0.9978` n `8`; equity avg `-0.0486` n `136`; fx avg `0.0019` n `6`; index avg `-0.0158` n `27`; metal avg `-0.0512` n `20`; unknown avg `0.637` n `866`
- 24h: commodity avg `-0.086` n `12`; crypto_alt avg `1.2305` n `233`; crypto_major avg `2.2677` n `8`; equity avg `-0.1204` n `136`; fx avg `0.036` n `6`; index avg `-0.1276` n `27`; metal avg `-0.3911` n `20`; unknown avg `6.5991` n `676`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
