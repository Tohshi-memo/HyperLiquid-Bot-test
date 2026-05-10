# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T05:37:14.644185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `12`; crypto_alt avg `0.1383` n `228`; crypto_major avg `0.0476` n `8`; equity avg `-0.0205` n `65`; fx avg `0.0` n `5`; index avg `0.0038` n `23`; metal avg `0.1241` n `18`; unknown avg `-0.2921` n `376`
- 1h: commodity avg `0.0208` n `12`; crypto_alt avg `0.2542` n `228`; crypto_major avg `0.0033` n `8`; equity avg `-0.0168` n `65`; fx avg `-0.0008` n `5`; index avg `0.0146` n `23`; metal avg `0.1569` n `18`; unknown avg `-0.4856` n `376`
- 4h: commodity avg `-0.1349` n `12`; crypto_alt avg `0.8538` n `228`; crypto_major avg `0.4692` n `8`; equity avg `0.3122` n `65`; fx avg `0.0023` n `5`; index avg `0.0599` n `23`; metal avg `0.3488` n `18`; unknown avg `-0.2618` n `376`
- 24h: commodity avg `0.2053` n `12`; crypto_alt avg `-1.3317` n `228`; crypto_major avg `-0.6545` n `8`; equity avg `0.9585` n `65`; fx avg `-0.0259` n `5`; index avg `0.3356` n `23`; metal avg `0.4945` n `18`; unknown avg `-0.4394` n `356`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
