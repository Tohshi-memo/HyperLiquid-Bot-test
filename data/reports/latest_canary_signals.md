# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T15:07:30.233712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2024` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0241` n `13`; crypto_alt avg `-0.2466` n `239`; crypto_major avg `-0.3926` n `8`; equity avg `-0.0919` n `162`; fx avg `-0.0012` n `6`; index avg `-0.0139` n `27`; metal avg `-0.0365` n `20`; unknown avg `18.5691` n `1258`
- 1h: commodity avg `0.0221` n `13`; crypto_alt avg `-0.6919` n `239`; crypto_major avg `-0.9036` n `8`; equity avg `-0.2314` n `162`; fx avg `-0.0019` n `6`; index avg `-0.0091` n `27`; metal avg `-0.0558` n `20`; unknown avg `18.7839` n `1260`
- 4h: commodity avg `-0.0701` n `13`; crypto_alt avg `-1.012` n `239`; crypto_major avg `-1.2165` n `8`; equity avg `-0.3196` n `162`; fx avg `-0.026` n `6`; index avg `-0.0141` n `27`; metal avg `-0.0552` n `20`; unknown avg `17.3065` n `1251`
- 24h: commodity avg `-0.0048` n `13`; crypto_alt avg `-2.9819` n `239`; crypto_major avg `-2.3685` n `8`; equity avg `-0.6426` n `162`; fx avg `-0.0142` n `6`; index avg `-0.043` n `27`; metal avg `-0.3128` n `20`; unknown avg `5.1541` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
