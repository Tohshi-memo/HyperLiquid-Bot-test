# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T09:37:12.289913+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.0051` n `228`; crypto_major avg `0.0318` n `8`; equity avg `0.0031` n `65`; fx avg `0.0` n `5`; index avg `-0.067` n `23`; metal avg `-0.0013` n `18`; unknown avg `-0.1817` n `376`
- 1h: commodity avg `-0.0056` n `12`; crypto_alt avg `-0.6533` n `228`; crypto_major avg `-0.1715` n `8`; equity avg `-0.1091` n `65`; fx avg `-0.0008` n `5`; index avg `-0.0373` n `23`; metal avg `-0.0009` n `18`; unknown avg `-0.3092` n `376`
- 4h: commodity avg `0.0149` n `12`; crypto_alt avg `-0.9224` n `228`; crypto_major avg `-0.2668` n `8`; equity avg `0.0307` n `65`; fx avg `0.0006` n `5`; index avg `0.0462` n `23`; metal avg `-0.0138` n `18`; unknown avg `-0.3861` n `356`
- 24h: commodity avg `0.0436` n `12`; crypto_alt avg `3.1092` n `228`; crypto_major avg `2.1557` n `8`; equity avg `2.6775` n `65`; fx avg `-0.0115` n `5`; index avg `1.1628` n `23`; metal avg `-0.0959` n `18`; unknown avg `0.5358` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
