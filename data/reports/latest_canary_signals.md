# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T23:37:25.610388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3296` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0185` n `12`; crypto_alt avg `-0.1325` n `228`; crypto_major avg `-0.2752` n `8`; equity avg `-0.1115` n `74`; fx avg `-0.0227` n `6`; index avg `-0.0597` n `23`; metal avg `-0.1615` n `18`; unknown avg `-0.1633` n `547`
- 1h: commodity avg `-0.0345` n `12`; crypto_alt avg `-0.1837` n `228`; crypto_major avg `-0.3947` n `8`; equity avg `-0.1591` n `74`; fx avg `-0.0279` n `6`; index avg `-0.0647` n `23`; metal avg `-0.4897` n `18`; unknown avg `-0.213` n `547`
- 4h: commodity avg `0.3117` n `12`; crypto_alt avg `-0.4648` n `228`; crypto_major avg `-0.9095` n `8`; equity avg `-0.3185` n `74`; fx avg `-0.0494` n `6`; index avg `0.4201` n `23`; metal avg `-0.5397` n `18`; unknown avg `-0.1906` n `547`
- 24h: commodity avg `-0.5916` n `12`; crypto_alt avg `-1.3435` n `228`; crypto_major avg `-3.2736` n `8`; equity avg `-2.4806` n `74`; fx avg `0.0574` n `6`; index avg `-1.0679` n `23`; metal avg `-1.9378` n `18`; unknown avg `-0.4347` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.045`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0412`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.038`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0362`, n `668`, weak_sample_signal
