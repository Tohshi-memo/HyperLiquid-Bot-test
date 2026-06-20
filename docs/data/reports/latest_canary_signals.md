# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T22:37:25.456862+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `12`; crypto_alt avg `0.187` n `228`; crypto_major avg `0.2639` n `8`; equity avg `0.0559` n `78`; fx avg `0.0024` n `6`; index avg `0.0178` n `23`; metal avg `0.016` n `18`; unknown avg `9.2403` n `701`
- 1h: commodity avg `-0.0418` n `12`; crypto_alt avg `0.4468` n `228`; crypto_major avg `0.6129` n `8`; equity avg `0.1101` n `78`; fx avg `0.0141` n `6`; index avg `0.0368` n `23`; metal avg `0.0375` n `18`; unknown avg `0.2834` n `701`
- 4h: commodity avg `-0.0158` n `12`; crypto_alt avg `0.6327` n `228`; crypto_major avg `0.972` n `8`; equity avg `0.2838` n `78`; fx avg `0.003` n `6`; index avg `0.0396` n `23`; metal avg `0.033` n `18`; unknown avg `-0.3439` n `701`
- 24h: commodity avg `0.1472` n `12`; crypto_alt avg `1.3129` n `228`; crypto_major avg `1.9188` n `8`; equity avg `0.6101` n `78`; fx avg `0.0911` n `6`; index avg `0.1039` n `23`; metal avg `-0.0186` n `18`; unknown avg `-0.2957` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
