# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T14:37:35.289773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3227` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0867` n `13`; crypto_alt avg `-0.1076` n `239`; crypto_major avg `-0.2069` n `8`; equity avg `-0.3749` n `165`; fx avg `0.0051` n `6`; index avg `-0.0058` n `27`; metal avg `-0.03` n `20`; unknown avg `228.5555` n `1262`
- 1h: commodity avg `-0.3016` n `13`; crypto_alt avg `0.5163` n `239`; crypto_major avg `0.7931` n `8`; equity avg `1.0388` n `165`; fx avg `-0.0147` n `6`; index avg `0.146` n `27`; metal avg `0.1461` n `20`; unknown avg `7.6675` n `1260`
- 4h: commodity avg `0.2207` n `13`; crypto_alt avg `-1.2883` n `239`; crypto_major avg `-1.3786` n `8`; equity avg `-0.7182` n `165`; fx avg `0.0334` n `6`; index avg `-0.0559` n `27`; metal avg `-0.1482` n `20`; unknown avg `322.866` n `1252`
- 24h: commodity avg `-0.6016` n `13`; crypto_alt avg `-4.5463` n `239`; crypto_major avg `-4.2955` n `8`; equity avg `-8.433` n `165`; fx avg `-0.042` n `6`; index avg `-0.766` n `27`; metal avg `-1.1722` n `20`; unknown avg `47.2692` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
