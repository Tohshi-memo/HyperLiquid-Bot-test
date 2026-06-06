# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T02:37:21.057991+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0372` n `12`; crypto_alt avg `-0.0195` n `228`; crypto_major avg `0.1098` n `8`; equity avg `-0.1464` n `74`; fx avg `-0.0016` n `6`; index avg `0.0096` n `23`; metal avg `-0.2864` n `18`; unknown avg `1.0666` n `425`
- 1h: commodity avg `0.0846` n `12`; crypto_alt avg `-0.9624` n `228`; crypto_major avg `-0.6918` n `8`; equity avg `-1.0444` n `74`; fx avg `-0.0041` n `6`; index avg `-0.4303` n `23`; metal avg `-0.4389` n `18`; unknown avg `0.024` n `425`
- 4h: commodity avg `0.5336` n `12`; crypto_alt avg `-1.1581` n `228`; crypto_major avg `-0.8358` n `8`; equity avg `-1.7894` n `74`; fx avg `-0.0338` n `6`; index avg `-0.6278` n `23`; metal avg `-0.5949` n `18`; unknown avg `2.0755` n `425`
- 24h: commodity avg `-1.1488` n `12`; crypto_alt avg `-6.108` n `228`; crypto_major avg `-5.2777` n `8`; equity avg `-7.0715` n `74`; fx avg `-0.2085` n `6`; index avg `-4.2058` n `23`; metal avg `-4.1717` n `18`; unknown avg `-1.061` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
