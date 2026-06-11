# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T17:22:38.637821+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1501` n `12`; crypto_alt avg `-0.3302` n `228`; crypto_major avg `-0.2742` n `8`; equity avg `-0.338` n `74`; fx avg `0.0016` n `6`; index avg `-0.1104` n `23`; metal avg `-0.0595` n `18`; unknown avg `-0.0452` n `556`
- 1h: commodity avg `-0.403` n `12`; crypto_alt avg `-0.5805` n `228`; crypto_major avg `-0.4207` n `8`; equity avg `-0.6806` n `74`; fx avg `-0.0061` n `6`; index avg `-0.2925` n `23`; metal avg `-0.4953` n `18`; unknown avg `-0.7138` n `556`
- 4h: commodity avg `-0.6325` n `12`; crypto_alt avg `-0.5558` n `228`; crypto_major avg `-0.5557` n `8`; equity avg `-0.2061` n `74`; fx avg `-0.084` n `6`; index avg `-0.0291` n `23`; metal avg `0.0361` n `18`; unknown avg `-0.415` n `556`
- 24h: commodity avg `-1.006` n `12`; crypto_alt avg `0.4623` n `228`; crypto_major avg `0.3819` n `8`; equity avg `-0.1509` n `74`; fx avg `-0.0749` n `6`; index avg `0.1384` n `23`; metal avg `-0.5425` n `18`; unknown avg `1.2799` n `529`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
