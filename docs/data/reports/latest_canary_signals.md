# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T07:52:14.601307+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0223` n `12`; crypto_alt avg `-0.1258` n `228`; crypto_major avg `-0.0524` n `8`; equity avg `-0.048` n `65`; fx avg `0.0006` n `5`; index avg `-0.0061` n `23`; metal avg `0.0026` n `18`; unknown avg `0.0145` n `376`
- 1h: commodity avg `0.0274` n `12`; crypto_alt avg `-0.3193` n `228`; crypto_major avg `-0.123` n `8`; equity avg `-0.0998` n `65`; fx avg `0.0017` n `5`; index avg `0.0283` n `23`; metal avg `0.0139` n `18`; unknown avg `0.2483` n `376`
- 4h: commodity avg `0.1803` n `12`; crypto_alt avg `-0.328` n `228`; crypto_major avg `-0.1645` n `8`; equity avg `-0.0797` n `65`; fx avg `0.0198` n `5`; index avg `0.064` n `23`; metal avg `-0.0123` n `18`; unknown avg `0.0679` n `355`
- 24h: commodity avg `-0.0195` n `12`; crypto_alt avg `3.9565` n `228`; crypto_major avg `2.5416` n `8`; equity avg `3.0578` n `65`; fx avg `0.0138` n `5`; index avg `1.3401` n `23`; metal avg `0.1628` n `18`; unknown avg `1.0501` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
