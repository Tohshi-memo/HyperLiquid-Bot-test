# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T11:07:44.644763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0427` n `13`; crypto_alt avg `0.2088` n `239`; crypto_major avg `0.1525` n `8`; equity avg `0.5286` n `162`; fx avg `0.0072` n `6`; index avg `0.0424` n `27`; metal avg `0.0197` n `20`; unknown avg `158.7075` n `1260`
- 1h: commodity avg `0.0223` n `13`; crypto_alt avg `0.0016` n `239`; crypto_major avg `-0.1457` n `8`; equity avg `0.3394` n `162`; fx avg `0.0007` n `6`; index avg `0.0442` n `27`; metal avg `0.0842` n `20`; unknown avg `158.4132` n `1262`
- 4h: commodity avg `0.2416` n `13`; crypto_alt avg `-0.5779` n `239`; crypto_major avg `-0.8049` n `8`; equity avg `-0.4667` n `162`; fx avg `-0.0538` n `6`; index avg `-0.0284` n `27`; metal avg `-0.1141` n `20`; unknown avg `204.2658` n `1222`
- 24h: commodity avg `-0.8017` n `13`; crypto_alt avg `-0.0268` n `239`; crypto_major avg `-0.0732` n `8`; equity avg `-2.8374` n `162`; fx avg `-0.0597` n `6`; index avg `-0.2843` n `27`; metal avg `-0.1894` n `20`; unknown avg `11.2114` n `1113`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
