# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T14:52:31.737668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.3749` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0606` n `12`; crypto_alt avg `-0.9886` n `234`; crypto_major avg `-0.8384` n `8`; equity avg `-0.5889` n `141`; fx avg `0.0035` n `6`; index avg `-0.1254` n `26`; metal avg `-0.1554` n `20`; unknown avg `9.729` n `962`
- 1h: commodity avg `0.1712` n `12`; crypto_alt avg `-2.0264` n `234`; crypto_major avg `-1.5598` n `8`; equity avg `-1.0724` n `141`; fx avg `0.0088` n `6`; index avg `-0.1849` n `26`; metal avg `-0.2736` n `20`; unknown avg `121.1452` n `910`
- 4h: commodity avg `-0.0963` n `12`; crypto_alt avg `-1.4092` n `234`; crypto_major avg `-0.9299` n `8`; equity avg `-1.2702` n `141`; fx avg `0.0103` n `6`; index avg `-0.1858` n `26`; metal avg `-0.3239` n `20`; unknown avg `42.3949` n `904`
- 24h: commodity avg `-0.1326` n `12`; crypto_alt avg `-4.0779` n `234`; crypto_major avg `-2.7308` n `8`; equity avg `-3.8462` n `141`; fx avg `0.0386` n `6`; index avg `-0.4186` n `26`; metal avg `-1.1578` n `20`; unknown avg `13.7147` n `786`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.2005`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1877`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
