# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T16:37:36.174433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0469` n `13`; crypto_alt avg `-0.1099` n `235`; crypto_major avg `-0.1336` n `8`; equity avg `0.149` n `151`; fx avg `-0.0147` n `6`; index avg `0.0305` n `26`; metal avg `0.0076` n `20`; unknown avg `0.0768` n `1135`
- 1h: commodity avg `0.0503` n `13`; crypto_alt avg `0.3963` n `235`; crypto_major avg `0.2879` n `8`; equity avg `0.8087` n `151`; fx avg `-0.0143` n `6`; index avg `0.1084` n `26`; metal avg `-0.0379` n `20`; unknown avg `1.1351` n `1127`
- 4h: commodity avg `0.797` n `13`; crypto_alt avg `0.4136` n `235`; crypto_major avg `0.3126` n `8`; equity avg `0.7375` n `151`; fx avg `0.0123` n `6`; index avg `0.0708` n `26`; metal avg `-0.287` n `20`; unknown avg `0.8454` n `1091`
- 24h: commodity avg `0.4467` n `13`; crypto_alt avg `-2.1041` n `235`; crypto_major avg `-0.8124` n `8`; equity avg `-1.0048` n `151`; fx avg `0.1429` n `6`; index avg `-0.2135` n `26`; metal avg `-0.2577` n `20`; unknown avg `0.1698` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1619`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1473`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1262`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0961`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0909`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
