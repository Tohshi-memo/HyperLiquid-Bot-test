# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T00:52:32.021681+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `13`; crypto_alt avg `-0.061` n `239`; crypto_major avg `-0.0602` n `8`; equity avg `-0.0499` n `166`; fx avg `-0.0077` n `6`; index avg `-0.0062` n `27`; metal avg `0.0097` n `20`; unknown avg `22.6806` n `1263`
- 1h: commodity avg `0.011` n `13`; crypto_alt avg `-0.1601` n `239`; crypto_major avg `-0.0269` n `8`; equity avg `0.0369` n `166`; fx avg `-0.0019` n `6`; index avg `0.0085` n `27`; metal avg `0.0023` n `20`; unknown avg `198.0861` n `1255`
- 4h: commodity avg `-0.0046` n `13`; crypto_alt avg `-0.1264` n `239`; crypto_major avg `-0.2014` n `8`; equity avg `0.1158` n `166`; fx avg `-0.0002` n `6`; index avg `0.0374` n `27`; metal avg `-0.04` n `20`; unknown avg `23.2648` n `1218`
- 24h: commodity avg `0.0599` n `13`; crypto_alt avg `0.2493` n `239`; crypto_major avg `1.6736` n `8`; equity avg `0.5795` n `166`; fx avg `-0.0456` n `6`; index avg `0.184` n `27`; metal avg `0.1041` n `20`; unknown avg `257.9507` n `1084`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
