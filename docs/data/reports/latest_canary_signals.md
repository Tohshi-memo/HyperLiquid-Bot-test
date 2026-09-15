# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T12:07:29.381035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0663` n `12`; crypto_alt avg `0.1621` n `233`; crypto_major avg `0.1178` n `8`; equity avg `0.0051` n `136`; fx avg `0.0157` n `6`; index avg `-0.0018` n `27`; metal avg `-0.0225` n `20`; unknown avg `1.9351` n `906`
- 1h: commodity avg `0.0223` n `12`; crypto_alt avg `-0.2122` n `233`; crypto_major avg `-0.1674` n `8`; equity avg `-0.054` n `136`; fx avg `0.0206` n `6`; index avg `0.0158` n `27`; metal avg `0.0145` n `20`; unknown avg `2.7232` n `906`
- 4h: commodity avg `-0.2222` n `12`; crypto_alt avg `0.1761` n `233`; crypto_major avg `0.4349` n `8`; equity avg `0.663` n `136`; fx avg `-0.0227` n `6`; index avg `0.1727` n `27`; metal avg `0.2642` n `20`; unknown avg `1.2967` n `898`
- 24h: commodity avg `-0.1385` n `12`; crypto_alt avg `-1.4574` n `233`; crypto_major avg `-0.8004` n `8`; equity avg `0.7797` n `136`; fx avg `0.1808` n `6`; index avg `0.1027` n `27`; metal avg `-0.0025` n `20`; unknown avg `-0.6047` n `818`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
