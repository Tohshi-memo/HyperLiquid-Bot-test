# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T13:37:25.155795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2761` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0815` n `13`; crypto_alt avg `-0.2257` n `239`; crypto_major avg `-0.2796` n `8`; equity avg `-0.3659` n `165`; fx avg `-0.0149` n `6`; index avg `-0.033` n `27`; metal avg `-0.0174` n `20`; unknown avg `158.3752` n `1262`
- 1h: commodity avg `0.258` n `13`; crypto_alt avg `-0.6896` n `239`; crypto_major avg `-0.7665` n `8`; equity avg `-0.6119` n `165`; fx avg `0.0036` n `6`; index avg `-0.0643` n `27`; metal avg `-0.1451` n `20`; unknown avg `158.9785` n `1260`
- 4h: commodity avg `0.5672` n `13`; crypto_alt avg `-1.6197` n `239`; crypto_major avg `-1.4125` n `8`; equity avg `-1.072` n `165`; fx avg `0.0488` n `6`; index avg `-0.1364` n `27`; metal avg `-0.0974` n `20`; unknown avg `177.1084` n `1248`
- 24h: commodity avg `-0.2473` n `13`; crypto_alt avg `-5.0805` n `239`; crypto_major avg `-4.831` n `8`; equity avg `-8.5987` n `165`; fx avg `-0.0282` n `6`; index avg `-0.862` n `27`; metal avg `-1.3654` n `20`; unknown avg `23.5748` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
