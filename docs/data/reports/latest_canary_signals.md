# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T17:52:35.622822+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0097` n `13`; crypto_alt avg `0.3299` n `239`; crypto_major avg `0.2879` n `8`; equity avg `0.2954` n `162`; fx avg `-0.0232` n `6`; index avg `0.024` n `27`; metal avg `0.0025` n `20`; unknown avg `0.1625` n `1259`
- 1h: commodity avg `0.1221` n `13`; crypto_alt avg `0.2855` n `239`; crypto_major avg `0.3338` n `8`; equity avg `0.1573` n `162`; fx avg `-0.0152` n `6`; index avg `0.0131` n `27`; metal avg `-0.0497` n `20`; unknown avg `42.7484` n `1253`
- 4h: commodity avg `0.1987` n `13`; crypto_alt avg `0.3911` n `239`; crypto_major avg `0.2571` n `8`; equity avg `1.6615` n `162`; fx avg `-0.0727` n `6`; index avg `0.189` n `27`; metal avg `-0.0811` n `20`; unknown avg `61.5445` n `1229`
- 24h: commodity avg `0.3992` n `13`; crypto_alt avg `-3.3564` n `239`; crypto_major avg `-3.3998` n `8`; equity avg `-2.7704` n `162`; fx avg `-0.1468` n `6`; index avg `-0.1223` n `27`; metal avg `-0.8373` n `20`; unknown avg `22.3381` n `1139`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
