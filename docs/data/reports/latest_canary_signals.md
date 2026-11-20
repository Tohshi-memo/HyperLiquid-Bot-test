# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T01:22:28.054109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0349` n `13`; crypto_alt avg `-0.3317` n `239`; crypto_major avg `-0.2468` n `8`; equity avg `-0.5275` n `165`; fx avg `-0.0118` n `6`; index avg `-0.0465` n `27`; metal avg `-0.1969` n `20`; unknown avg `0.366` n `1260`
- 1h: commodity avg `-0.0653` n `13`; crypto_alt avg `-0.3621` n `239`; crypto_major avg `-0.228` n `8`; equity avg `-0.7165` n `165`; fx avg `-0.0258` n `6`; index avg `-0.1194` n `27`; metal avg `-0.4338` n `20`; unknown avg `-0.0526` n `1256`
- 4h: commodity avg `-0.0932` n `13`; crypto_alt avg `0.2951` n `239`; crypto_major avg `0.5647` n `8`; equity avg `-0.8906` n `165`; fx avg `-0.0073` n `6`; index avg `-0.085` n `27`; metal avg `-0.6318` n `20`; unknown avg `9.5964` n `1242`
- 24h: commodity avg `-0.1051` n `13`; crypto_alt avg `-1.1978` n `239`; crypto_major avg `-0.6821` n `8`; equity avg `-5.2998` n `165`; fx avg `-0.0197` n `6`; index avg `-0.4091` n `27`; metal avg `-1.4996` n `20`; unknown avg `8.606` n `1172`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
