# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T22:07:42.318038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `0.1813` n `230`; crypto_major avg `0.2145` n `8`; equity avg `0.0686` n `102`; fx avg `0.0068` n `6`; index avg `0.0052` n `25`; metal avg `-0.0064` n `20`; unknown avg `-0.0643` n `779`
- 1h: commodity avg `0.012` n `12`; crypto_alt avg `0.2154` n `230`; crypto_major avg `0.2008` n `8`; equity avg `0.4327` n `102`; fx avg `0.0063` n `6`; index avg `0.0597` n `25`; metal avg `0.0058` n `20`; unknown avg `0.0606` n `779`
- 4h: commodity avg `-0.0217` n `12`; crypto_alt avg `0.0381` n `230`; crypto_major avg `0.0543` n `8`; equity avg `1.3975` n `102`; fx avg `0.0612` n `6`; index avg `0.1592` n `25`; metal avg `0.1033` n `20`; unknown avg `-0.1172` n `779`
- 24h: commodity avg `-0.0401` n `12`; crypto_alt avg `1.0821` n `230`; crypto_major avg `1.7167` n `8`; equity avg `8.0331` n `102`; fx avg `-0.4055` n `6`; index avg `0.9549` n `25`; metal avg `0.6203` n `20`; unknown avg `0.1482` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
