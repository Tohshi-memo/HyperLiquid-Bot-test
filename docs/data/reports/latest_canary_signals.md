# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T08:22:20.685876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `12`; crypto_alt avg `0.1197` n `228`; crypto_major avg `0.0618` n `8`; equity avg `-0.0274` n `69`; fx avg `0.0086` n `6`; index avg `-0.0067` n `23`; metal avg `0.006` n `18`; unknown avg `-0.163` n `421`
- 1h: commodity avg `0.0135` n `12`; crypto_alt avg `0.0858` n `228`; crypto_major avg `0.0518` n `8`; equity avg `0.1963` n `69`; fx avg `-0.0146` n `6`; index avg `0.0936` n `23`; metal avg `0.0142` n `18`; unknown avg `-0.0011` n `421`
- 4h: commodity avg `0.1361` n `12`; crypto_alt avg `-0.4169` n `228`; crypto_major avg `-0.5039` n `8`; equity avg `0.4187` n `69`; fx avg `0.0002` n `6`; index avg `0.0191` n `23`; metal avg `0.0124` n `18`; unknown avg `0.0907` n `401`
- 24h: commodity avg `0.257` n `12`; crypto_alt avg `0.3638` n `228`; crypto_major avg `1.7998` n `8`; equity avg `1.1951` n `69`; fx avg `0.0606` n `6`; index avg `-0.038` n `23`; metal avg `-0.0219` n `18`; unknown avg `0.8287` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
