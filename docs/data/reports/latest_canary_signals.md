# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T00:52:25.850030+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `0.1052` n `232`; crypto_major avg `-0.003` n `8`; equity avg `-0.01` n `130`; fx avg `0.0007` n `6`; index avg `0.0045` n `26`; metal avg `0.041` n `20`; unknown avg `0.1671` n `792`
- 1h: commodity avg `0.0589` n `12`; crypto_alt avg `0.6835` n `232`; crypto_major avg `0.2652` n `8`; equity avg `0.0217` n `130`; fx avg `0.0297` n `6`; index avg `0.0062` n `26`; metal avg `0.1228` n `20`; unknown avg `1.1981` n `790`
- 4h: commodity avg `0.0846` n `12`; crypto_alt avg `0.6942` n `232`; crypto_major avg `-0.0819` n `8`; equity avg `0.0507` n `130`; fx avg `0.0381` n `6`; index avg `0.0267` n `26`; metal avg `0.1404` n `20`; unknown avg `1.6945` n `784`
- 24h: commodity avg `0.6589` n `12`; crypto_alt avg `1.9515` n `231`; crypto_major avg `1.4993` n `8`; equity avg `1.0079` n `130`; fx avg `-0.0794` n `6`; index avg `0.1297` n `26`; metal avg `-0.193` n `20`; unknown avg `0.1268` n `739`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
