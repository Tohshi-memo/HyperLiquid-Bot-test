# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T09:52:30.857713+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0238` n `13`; crypto_alt avg `0.0886` n `239`; crypto_major avg `0.0537` n `8`; equity avg `0.3132` n `162`; fx avg `0.0223` n `6`; index avg `0.0376` n `27`; metal avg `0.0312` n `20`; unknown avg `157.9293` n `1266`
- 1h: commodity avg `0.1591` n `13`; crypto_alt avg `-0.4083` n `239`; crypto_major avg `-0.2326` n `8`; equity avg `-0.6737` n `162`; fx avg `0.0033` n `6`; index avg `-0.0511` n `27`; metal avg `-0.0721` n `20`; unknown avg `18.7216` n `1260`
- 4h: commodity avg `0.3146` n `13`; crypto_alt avg `-0.7666` n `239`; crypto_major avg `-0.8248` n `8`; equity avg `-0.9552` n `162`; fx avg `-0.0314` n `6`; index avg `-0.0588` n `27`; metal avg `-0.1893` n `20`; unknown avg `212.8183` n `1172`
- 24h: commodity avg `-0.7814` n `13`; crypto_alt avg `0.6854` n `239`; crypto_major avg `1.0973` n `8`; equity avg `-2.9383` n `162`; fx avg `-0.0079` n `6`; index avg `-0.3095` n `27`; metal avg `-0.0365` n `20`; unknown avg `17.5422` n `1115`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
