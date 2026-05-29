# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T23:22:21.230825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0411` n `12`; crypto_alt avg `-0.1678` n `228`; crypto_major avg `-0.2505` n `8`; equity avg `0.0158` n `69`; fx avg `-0.0153` n `6`; index avg `0.0017` n `23`; metal avg `-0.0191` n `18`; unknown avg `-0.058` n `419`
- 1h: commodity avg `0.1957` n `12`; crypto_alt avg `-0.1428` n `228`; crypto_major avg `-0.3044` n `8`; equity avg `-0.0149` n `69`; fx avg `-0.0158` n `6`; index avg `-0.0332` n `23`; metal avg `-0.001` n `18`; unknown avg `-0.3966` n `419`
- 4h: commodity avg `0.3376` n `12`; crypto_alt avg `0.2761` n `228`; crypto_major avg `-0.0867` n `8`; equity avg `0.4142` n `69`; fx avg `-0.0437` n `6`; index avg `0.0464` n `23`; metal avg `-0.2507` n `18`; unknown avg `-0.2567` n `419`
- 24h: commodity avg `-0.3417` n `12`; crypto_alt avg `0.5997` n `228`; crypto_major avg `0.5749` n `8`; equity avg `0.7944` n `69`; fx avg `0.168` n `6`; index avg `0.0591` n `23`; metal avg `0.03` n `18`; unknown avg `0.4609` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
