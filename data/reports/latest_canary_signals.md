# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T02:37:31.972600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3717` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.0433` n `229`; crypto_major avg `-0.0952` n `8`; equity avg `0.0366` n `88`; fx avg `-0.0041` n `6`; index avg `-0.0051` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.2241` n `765`
- 1h: commodity avg `0.03` n `12`; crypto_alt avg `-0.1941` n `229`; crypto_major avg `-0.2573` n `8`; equity avg `0.0594` n `88`; fx avg `-0.0019` n `6`; index avg `0.0312` n `25`; metal avg `-0.024` n `20`; unknown avg `-0.413` n `765`
- 4h: commodity avg `0.0233` n `12`; crypto_alt avg `-1.1807` n `229`; crypto_major avg `-1.3819` n `8`; equity avg `0.0518` n `88`; fx avg `0.0028` n `6`; index avg `-0.0102` n `25`; metal avg `-0.0088` n `20`; unknown avg `-0.5269` n `763`
- 24h: commodity avg `0.054` n `12`; crypto_alt avg `-0.5664` n `229`; crypto_major avg `-0.4336` n `8`; equity avg `0.2568` n `88`; fx avg `-0.0134` n `6`; index avg `0.0435` n `25`; metal avg `0.097` n `20`; unknown avg `-0.935` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
