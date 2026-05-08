# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T13:22:21.079170+00:00`
- Correlation status: `ready`
- Asset price records: `649`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1203` n `12`; crypto_alt avg `-0.077` n `228`; crypto_major avg `-0.0697` n `8`; equity avg `-0.0321` n `65`; fx avg `-0.0101` n `5`; index avg `-0.0136` n `23`; metal avg `0.0182` n `18`; unknown avg `0.086` n `375`
- 1h: commodity avg `0.0523` n `12`; crypto_alt avg `-0.2621` n `228`; crypto_major avg `-0.3558` n `8`; equity avg `0.1255` n `65`; fx avg `-0.0358` n `5`; index avg `0.119` n `23`; metal avg `0.0487` n `18`; unknown avg `-0.1365` n `375`
- 4h: commodity avg `0.244` n `12`; crypto_alt avg `-0.364` n `228`; crypto_major avg `-0.3884` n `8`; equity avg `-0.0224` n `65`; fx avg `-0.0274` n `5`; index avg `0.0974` n `23`; metal avg `-0.1583` n `18`; unknown avg `-0.3163` n `375`
- 24h: commodity avg `1.9218` n `12`; crypto_alt avg `0.1274` n `228`; crypto_major avg `-1.7579` n `8`; equity avg `-0.4403` n `65`; fx avg `0.2153` n `5`; index avg `-0.1952` n `23`; metal avg `-0.753` n `18`; unknown avg `-0.5175` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1274`, n `641`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1251`, n `641`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `645`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0988`, n `645`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `645`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0912`, n `641`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.09`, n `645`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0896`, n `641`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.07`, n `645`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0682`, n `645`, weak_sample_signal
