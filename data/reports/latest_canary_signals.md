# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T06:22:28.582758+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0268` n `13`; crypto_alt avg `-0.2941` n `239`; crypto_major avg `-0.3506` n `8`; equity avg `-0.3833` n `166`; fx avg `-0.0052` n `6`; index avg `-0.0495` n `27`; metal avg `-0.136` n `20`; unknown avg `269.3373` n `1264`
- 1h: commodity avg `-0.095` n `13`; crypto_alt avg `-0.0021` n `239`; crypto_major avg `-0.076` n `8`; equity avg `0.0538` n `166`; fx avg `0.0163` n `6`; index avg `-0.0436` n `27`; metal avg `0.0083` n `20`; unknown avg `425.4427` n `1242`
- 4h: commodity avg `-0.0495` n `13`; crypto_alt avg `1.2998` n `239`; crypto_major avg `1.2282` n `8`; equity avg `1.0972` n `166`; fx avg `0.043` n `6`; index avg `-0.0045` n `27`; metal avg `0.2965` n `20`; unknown avg `1.2592` n `1229`
- 24h: commodity avg `-0.4233` n `13`; crypto_alt avg `2.3027` n `239`; crypto_major avg `3.2135` n `8`; equity avg `2.403` n `166`; fx avg `0.2364` n `6`; index avg `0.1515` n `27`; metal avg `0.484` n `20`; unknown avg `294.6328` n `1017`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
