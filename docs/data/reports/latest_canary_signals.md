# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T09:07:27.603364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0352` n `12`; crypto_alt avg `0.0104` n `233`; crypto_major avg `0.0689` n `8`; equity avg `0.008` n `136`; fx avg `-0.0149` n `6`; index avg `0.0002` n `27`; metal avg `0.0156` n `20`; unknown avg `1.1117` n `906`
- 1h: commodity avg `-0.0659` n `12`; crypto_alt avg `0.3403` n `233`; crypto_major avg `0.2589` n `8`; equity avg `0.0311` n `136`; fx avg `-0.004` n `6`; index avg `0.0144` n `27`; metal avg `0.0826` n `20`; unknown avg `16.6424` n `900`
- 4h: commodity avg `0.0525` n `12`; crypto_alt avg `-0.705` n `233`; crypto_major avg `-0.6257` n `8`; equity avg `-0.3033` n `136`; fx avg `0.1083` n `6`; index avg `-0.0729` n `27`; metal avg `-0.2227` n `20`; unknown avg `20.1616` n `876`
- 24h: commodity avg `-0.0286` n `12`; crypto_alt avg `-1.3352` n `233`; crypto_major avg `-0.8469` n `8`; equity avg `-0.1325` n `136`; fx avg `0.2448` n `6`; index avg `-0.0664` n `27`; metal avg `-0.2592` n `20`; unknown avg `4.8635` n `820`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
