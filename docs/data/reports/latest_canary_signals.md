# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T23:07:17.410503+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1024` n `12`; crypto_alt avg `0.2104` n `228`; crypto_major avg `0.1995` n `8`; equity avg `-0.0239` n `69`; fx avg `-0.0019` n `6`; index avg `-0.0277` n `23`; metal avg `0.0073` n `18`; unknown avg `-0.1427` n `419`
- 1h: commodity avg `0.2023` n `12`; crypto_alt avg `0.4835` n `228`; crypto_major avg `0.2595` n `8`; equity avg `0.0409` n `69`; fx avg `0.0014` n `6`; index avg `-0.0487` n `23`; metal avg `0.0655` n `18`; unknown avg `-0.3139` n `419`
- 4h: commodity avg `0.2672` n `12`; crypto_alt avg `-0.0802` n `228`; crypto_major avg `-0.0434` n `8`; equity avg `0.4717` n `69`; fx avg `-0.0216` n `6`; index avg `0.055` n `23`; metal avg `-0.1959` n `18`; unknown avg `-0.6574` n `419`
- 24h: commodity avg `-0.3907` n `12`; crypto_alt avg `0.7517` n `228`; crypto_major avg `0.7608` n `8`; equity avg `0.895` n `69`; fx avg `0.1835` n `6`; index avg `0.0784` n `23`; metal avg `0.0699` n `18`; unknown avg `0.4124` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
