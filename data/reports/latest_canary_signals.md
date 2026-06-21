# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T20:07:26.266850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `-0.0634` n `228`; crypto_major avg `-0.0121` n `8`; equity avg `-0.0011` n `78`; fx avg `-0.0223` n `6`; index avg `0.0091` n `23`; metal avg `0.0018` n `18`; unknown avg `0.0137` n `702`
- 1h: commodity avg `-0.0084` n `12`; crypto_alt avg `-0.1034` n `228`; crypto_major avg `0.1566` n `8`; equity avg `-0.0` n `78`; fx avg `-0.0438` n `6`; index avg `0.026` n `23`; metal avg `-0.0037` n `18`; unknown avg `0.2847` n `694`
- 4h: commodity avg `0.2333` n `12`; crypto_alt avg `-0.2685` n `228`; crypto_major avg `0.2075` n `8`; equity avg `-0.0276` n `78`; fx avg `-0.1381` n `6`; index avg `0.0104` n `23`; metal avg `-0.0782` n `18`; unknown avg `-0.0338` n `694`
- 24h: commodity avg `0.295` n `12`; crypto_alt avg `1.4396` n `228`; crypto_major avg `0.432` n `8`; equity avg `0.3029` n `78`; fx avg `-0.1163` n `6`; index avg `0.037` n `23`; metal avg `-0.0897` n `18`; unknown avg `0.3013` n `645`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
