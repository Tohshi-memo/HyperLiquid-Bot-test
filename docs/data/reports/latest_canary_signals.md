# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T04:52:34.176023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.0227` n `234`; crypto_major avg `0.0049` n `8`; equity avg `-0.0004` n `141`; fx avg `-0.0058` n `6`; index avg `-0.0031` n `26`; metal avg `0.0204` n `20`; unknown avg `-0.0562` n `963`
- 1h: commodity avg `0.0437` n `12`; crypto_alt avg `0.153` n `234`; crypto_major avg `-0.0175` n `8`; equity avg `-0.1002` n `141`; fx avg `-0.0093` n `6`; index avg `-0.0381` n `26`; metal avg `-0.0579` n `20`; unknown avg `11.6803` n `955`
- 4h: commodity avg `0.1509` n `12`; crypto_alt avg `-0.9549` n `234`; crypto_major avg `-0.275` n `8`; equity avg `-0.2907` n `141`; fx avg `-0.0524` n `6`; index avg `-0.057` n `26`; metal avg `-0.0371` n `20`; unknown avg `-0.0383` n `955`
- 24h: commodity avg `0.0806` n `12`; crypto_alt avg `-2.6915` n `234`; crypto_major avg `-1.1935` n `8`; equity avg `-2.2408` n `141`; fx avg `-0.0703` n `6`; index avg `-0.2565` n `26`; metal avg `-0.5162` n `20`; unknown avg `9.5673` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
