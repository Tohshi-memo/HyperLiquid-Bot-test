# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T16:52:32.465973+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0157` n `12`; crypto_alt avg `0.3401` n `228`; crypto_major avg `0.1235` n `8`; equity avg `0.0227` n `78`; fx avg `0.0174` n `6`; index avg `0.0069` n `23`; metal avg `-0.0035` n `18`; unknown avg `-0.0146` n `701`
- 1h: commodity avg `0.0598` n `12`; crypto_alt avg `-0.0403` n `228`; crypto_major avg `-0.3133` n `8`; equity avg `-0.0217` n `78`; fx avg `0.0226` n `6`; index avg `-0.0087` n `23`; metal avg `-0.0402` n `18`; unknown avg `0.0889` n `701`
- 4h: commodity avg `0.2348` n `12`; crypto_alt avg `0.574` n `228`; crypto_major avg `0.0506` n `8`; equity avg `0.0235` n `78`; fx avg `0.0316` n `6`; index avg `-0.0144` n `23`; metal avg `-0.0211` n `18`; unknown avg `0.0154` n `701`
- 24h: commodity avg `0.2667` n `12`; crypto_alt avg `0.7878` n `228`; crypto_major avg `1.3469` n `8`; equity avg `0.4163` n `78`; fx avg `0.0805` n `6`; index avg `0.0127` n `23`; metal avg `0.1735` n `18`; unknown avg `-0.1074` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
