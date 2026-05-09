# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T02:37:20.215115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0239` n `12`; crypto_alt avg `-0.0199` n `228`; crypto_major avg `0.0832` n `8`; equity avg `0.05` n `65`; fx avg `-0.0272` n `5`; index avg `0.0521` n `23`; metal avg `0.0658` n `18`; unknown avg `0.2421` n `375`
- 1h: commodity avg `0.1319` n `12`; crypto_alt avg `0.055` n `228`; crypto_major avg `0.1686` n `8`; equity avg `0.0631` n `65`; fx avg `-0.0212` n `5`; index avg `0.1679` n `23`; metal avg `0.1429` n `18`; unknown avg `0.8721` n `375`
- 4h: commodity avg `0.078` n `12`; crypto_alt avg `1.061` n `228`; crypto_major avg `0.749` n `8`; equity avg `0.1706` n `65`; fx avg `-0.0151` n `5`; index avg `0.1971` n `23`; metal avg `0.11` n `18`; unknown avg `0.2276` n `375`
- 24h: commodity avg `-0.515` n `12`; crypto_alt avg `5.0259` n `228`; crypto_major avg `2.9031` n `8`; equity avg `3.9203` n `65`; fx avg `0.0664` n `5`; index avg `1.5121` n `23`; metal avg `0.582` n `18`; unknown avg `1.7715` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
