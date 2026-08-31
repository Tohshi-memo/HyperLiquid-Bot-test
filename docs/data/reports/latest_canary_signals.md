# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T12:52:26.476445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0522` n `12`; crypto_alt avg `-0.3322` n `232`; crypto_major avg `-0.3129` n `8`; equity avg `-0.223` n `128`; fx avg `0.003` n `6`; index avg `-0.0324` n `26`; metal avg `-0.1122` n `20`; unknown avg `0.031` n `794`
- 1h: commodity avg `-0.256` n `12`; crypto_alt avg `-0.5421` n `232`; crypto_major avg `-0.4036` n `8`; equity avg `-0.2451` n `128`; fx avg `0.0344` n `6`; index avg `-0.0265` n `26`; metal avg `-0.1921` n `20`; unknown avg `0.1385` n `792`
- 4h: commodity avg `-0.0336` n `12`; crypto_alt avg `-0.6062` n `232`; crypto_major avg `-0.3611` n `8`; equity avg `-0.5149` n `128`; fx avg `0.0373` n `6`; index avg `-0.0869` n `26`; metal avg `-0.0865` n `20`; unknown avg `0.2024` n `791`
- 24h: commodity avg `0.4777` n `12`; crypto_alt avg `-1.5247` n `231`; crypto_major avg `-1.8463` n `8`; equity avg `-0.7749` n `128`; fx avg `-0.1116` n `6`; index avg `-0.1445` n `26`; metal avg `-0.3331` n `20`; unknown avg `-0.1417` n `761`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
