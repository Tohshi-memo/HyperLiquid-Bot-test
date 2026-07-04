# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T15:19:38.519171+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0401` n `12`; crypto_alt avg `0.2853` n `229`; crypto_major avg `0.2435` n `8`; equity avg `0.0499` n `88`; fx avg `-0.0092` n `6`; index avg `-0.0004` n `25`; metal avg `0.0` n `20`; unknown avg `0.1695` n `765`
- 1h: commodity avg `0.0296` n `12`; crypto_alt avg `0.561` n `229`; crypto_major avg `0.4919` n `8`; equity avg `0.0664` n `88`; fx avg `0.0208` n `6`; index avg `-0.0014` n `25`; metal avg `0.0147` n `20`; unknown avg `0.147` n `765`
- 4h: commodity avg `-0.043` n `12`; crypto_alt avg `1.0577` n `229`; crypto_major avg `1.0223` n `8`; equity avg `0.0133` n `88`; fx avg `0.0324` n `6`; index avg `0.0019` n `25`; metal avg `0.0102` n `20`; unknown avg `0.0756` n `759`
- 24h: commodity avg `0.0901` n `12`; crypto_alt avg `1.1739` n `229`; crypto_major avg `1.7458` n `8`; equity avg `0.2903` n `88`; fx avg `-0.0324` n `6`; index avg `-0.0354` n `25`; metal avg `-0.0097` n `20`; unknown avg `2.0802` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
