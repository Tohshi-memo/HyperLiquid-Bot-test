# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T02:07:19.116977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.049` n `12`; crypto_alt avg `0.2582` n `228`; crypto_major avg `0.3133` n `8`; equity avg `0.0617` n `67`; fx avg `0.0032` n `6`; index avg `-0.0016` n `23`; metal avg `-0.0041` n `18`; unknown avg `0.5118` n `396`
- 1h: commodity avg `0.0097` n `12`; crypto_alt avg `0.2586` n `228`; crypto_major avg `0.134` n `8`; equity avg `0.1178` n `67`; fx avg `-0.0068` n `6`; index avg `0.0449` n `23`; metal avg `-0.0771` n `18`; unknown avg `0.9509` n `396`
- 4h: commodity avg `-0.0041` n `12`; crypto_alt avg `0.9829` n `228`; crypto_major avg `0.5484` n `8`; equity avg `0.3818` n `67`; fx avg `-0.1246` n `6`; index avg `0.218` n `23`; metal avg `0.429` n `18`; unknown avg `0.619` n `396`
- 24h: commodity avg `0.4218` n `12`; crypto_alt avg `-1.1453` n `228`; crypto_major avg `0.2029` n `8`; equity avg `0.2894` n `67`; fx avg `-0.0274` n `6`; index avg `-0.2227` n `23`; metal avg `0.6125` n `18`; unknown avg `-0.3796` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
