# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T22:07:29.879191+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.023` n `12`; crypto_alt avg `-0.1037` n `229`; crypto_major avg `-0.1157` n `8`; equity avg `0.0284` n `88`; fx avg `0.0009` n `6`; index avg `0.0006` n `25`; metal avg `0.0074` n `20`; unknown avg `0.0217` n `765`
- 1h: commodity avg `0.0623` n `12`; crypto_alt avg `-0.0525` n `229`; crypto_major avg `-0.1968` n `8`; equity avg `0.0721` n `88`; fx avg `0.0003` n `6`; index avg `-0.0064` n `25`; metal avg `0.0076` n `20`; unknown avg `-0.0439` n `765`
- 4h: commodity avg `-0.0111` n `12`; crypto_alt avg `0.731` n `229`; crypto_major avg `0.8319` n `8`; equity avg `-0.0013` n `88`; fx avg `-0.0123` n `6`; index avg `-0.0491` n `25`; metal avg `-0.009` n `20`; unknown avg `-0.2196` n `765`
- 24h: commodity avg `0.1659` n `12`; crypto_alt avg `3.3067` n `229`; crypto_major avg `3.5515` n `8`; equity avg `1.8615` n `88`; fx avg `-0.0712` n `6`; index avg `0.4549` n `25`; metal avg `0.5321` n `20`; unknown avg `5.3154` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
