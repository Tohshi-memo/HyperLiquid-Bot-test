# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T11:37:27.336906+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1462` n `12`; crypto_alt avg `-0.0088` n `228`; crypto_major avg `0.0752` n `8`; equity avg `0.2641` n `74`; fx avg `0.0021` n `6`; index avg `0.0778` n `23`; metal avg `0.0966` n `18`; unknown avg `0.168` n `556`
- 1h: commodity avg `-0.0093` n `12`; crypto_alt avg `0.0585` n `228`; crypto_major avg `0.3488` n `8`; equity avg `0.0316` n `74`; fx avg `0.0206` n `6`; index avg `-0.0454` n `23`; metal avg `-0.0759` n `18`; unknown avg `0.4669` n `556`
- 4h: commodity avg `-0.3409` n `12`; crypto_alt avg `0.4303` n `228`; crypto_major avg `0.6972` n `8`; equity avg `0.4608` n `74`; fx avg `-0.049` n `6`; index avg `0.1954` n `23`; metal avg `-0.4972` n `18`; unknown avg `1.1162` n `556`
- 24h: commodity avg `-0.9432` n `12`; crypto_alt avg `2.5771` n `228`; crypto_major avg `2.3923` n `8`; equity avg `1.6589` n `74`; fx avg `0.0212` n `6`; index avg `0.4394` n `23`; metal avg `-0.5007` n `18`; unknown avg `5.3864` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
