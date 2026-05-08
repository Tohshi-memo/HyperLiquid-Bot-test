# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T23:52:14.153779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `0.1201` n `228`; crypto_major avg `0.1207` n `8`; equity avg `-0.0009` n `65`; fx avg `-0.0008` n `5`; index avg `0.0017` n `23`; metal avg `-0.0082` n `18`; unknown avg `-0.2688` n `375`
- 1h: commodity avg `0.0031` n `12`; crypto_alt avg `-0.2243` n `228`; crypto_major avg `-0.1968` n `8`; equity avg `-0.032` n `65`; fx avg `0.0` n `5`; index avg `0.0631` n `23`; metal avg `-0.0856` n `18`; unknown avg `-0.3807` n `375`
- 4h: commodity avg `-0.1944` n `12`; crypto_alt avg `0.4797` n `228`; crypto_major avg `-0.0445` n `8`; equity avg `0.6073` n `65`; fx avg `-0.0103` n `5`; index avg `0.1769` n `23`; metal avg `-0.4254` n `18`; unknown avg `-0.4512` n `375`
- 24h: commodity avg `-0.7045` n `12`; crypto_alt avg `3.3115` n `228`; crypto_major avg `1.4663` n `8`; equity avg `4.0297` n `65`; fx avg `0.2189` n `5`; index avg `1.5937` n `23`; metal avg `0.5858` n `18`; unknown avg `0.8106` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
