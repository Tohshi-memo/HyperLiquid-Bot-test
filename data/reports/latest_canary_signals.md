# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T10:07:23.720397+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0056` n `12`; crypto_alt avg `-0.8849` n `228`; crypto_major avg `-0.6632` n `8`; equity avg `-0.1729` n `74`; fx avg `0.0067` n `6`; index avg `-0.0327` n `23`; metal avg `-0.0695` n `18`; unknown avg `-0.1478` n `425`
- 1h: commodity avg `-0.1783` n `12`; crypto_alt avg `-1.4367` n `228`; crypto_major avg `-1.2276` n `8`; equity avg `-0.1812` n `74`; fx avg `0.0066` n `6`; index avg `-0.4814` n `23`; metal avg `-0.1397` n `18`; unknown avg `-0.4003` n `425`
- 4h: commodity avg `-0.1275` n `12`; crypto_alt avg `-0.3585` n `228`; crypto_major avg `-0.6363` n `8`; equity avg `-0.3643` n `74`; fx avg `-0.0023` n `6`; index avg `0.0065` n `23`; metal avg `0.0663` n `18`; unknown avg `0.3058` n `425`
- 24h: commodity avg `-1.3573` n `12`; crypto_alt avg `-4.9668` n `228`; crypto_major avg `-4.2777` n `8`; equity avg `-7.0434` n `74`; fx avg `-0.2465` n `6`; index avg `-4.1176` n `23`; metal avg `-4.3463` n `18`; unknown avg `0.0501` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
