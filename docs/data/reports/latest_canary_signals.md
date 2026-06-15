# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T03:52:30.108596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0919` n `12`; crypto_alt avg `0.0884` n `228`; crypto_major avg `0.1332` n `8`; equity avg `0.0098` n `74`; fx avg `0.0048` n `6`; index avg `0.0156` n `23`; metal avg `0.0296` n `18`; unknown avg `0.6886` n `645`
- 1h: commodity avg `0.1925` n `12`; crypto_alt avg `0.2493` n `228`; crypto_major avg `0.3077` n `8`; equity avg `0.1398` n `74`; fx avg `0.0103` n `6`; index avg `0.1508` n `23`; metal avg `-0.2431` n `18`; unknown avg `-0.3637` n `637`
- 4h: commodity avg `-0.3393` n `12`; crypto_alt avg `0.5211` n `228`; crypto_major avg `0.2826` n `8`; equity avg `0.5894` n `74`; fx avg `0.0019` n `6`; index avg `0.5529` n `23`; metal avg `0.3409` n `18`; unknown avg `-0.702` n `629`
- 24h: commodity avg `-1.039` n `12`; crypto_alt avg `2.3566` n `228`; crypto_major avg `2.6199` n `8`; equity avg `1.8411` n `74`; fx avg `0.0151` n `6`; index avg `0.9296` n `23`; metal avg `2.0398` n `18`; unknown avg `3.238` n `585`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
