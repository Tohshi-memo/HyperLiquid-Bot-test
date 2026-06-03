# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T20:52:26.729031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0641` n `12`; crypto_alt avg `-0.7411` n `228`; crypto_major avg `-0.4859` n `8`; equity avg `-0.1791` n `73`; fx avg `-0.0096` n `6`; index avg `-0.0702` n `23`; metal avg `-0.0739` n `18`; unknown avg `-0.2329` n `419`
- 1h: commodity avg `0.1235` n `12`; crypto_alt avg `-1.0888` n `228`; crypto_major avg `-0.7398` n `8`; equity avg `-1.0411` n `73`; fx avg `0.0003` n `6`; index avg `-0.3366` n `23`; metal avg `-0.3401` n `18`; unknown avg `-0.3274` n `419`
- 4h: commodity avg `0.1608` n `12`; crypto_alt avg `-1.2312` n `228`; crypto_major avg `-1.1758` n `8`; equity avg `-0.8659` n `73`; fx avg `0.0199` n `6`; index avg `-0.1812` n `23`; metal avg `-0.461` n `18`; unknown avg `-0.6021` n `419`
- 24h: commodity avg `1.0065` n `12`; crypto_alt avg `-0.7195` n `228`; crypto_major avg `-3.0909` n `8`; equity avg `-3.1693` n `72`; fx avg `0.0591` n `6`; index avg `-0.6691` n `23`; metal avg `-2.4011` n `18`; unknown avg `-0.3007` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
