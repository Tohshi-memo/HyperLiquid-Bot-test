# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T12:37:20.460916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1739` n `12`; crypto_alt avg `-0.4153` n `228`; crypto_major avg `-0.2024` n `8`; equity avg `-0.0751` n `69`; fx avg `0.019` n `6`; index avg `-0.0257` n `23`; metal avg `0.0672` n `18`; unknown avg `-0.0259` n `417`
- 1h: commodity avg `0.1712` n `12`; crypto_alt avg `-0.7031` n `228`; crypto_major avg `-0.44` n `8`; equity avg `-0.0539` n `69`; fx avg `0.0175` n `6`; index avg `-0.0712` n `23`; metal avg `-0.2059` n `18`; unknown avg `-0.258` n `417`
- 4h: commodity avg `-0.2897` n `12`; crypto_alt avg `-0.9362` n `228`; crypto_major avg `-0.7813` n `8`; equity avg `-0.3147` n `69`; fx avg `-0.0097` n `6`; index avg `0.0684` n `23`; metal avg `0.1262` n `18`; unknown avg `-0.4014` n `417`
- 24h: commodity avg `0.4296` n `12`; crypto_alt avg `0.9788` n `228`; crypto_major avg `1.6289` n `8`; equity avg `2.9628` n `69`; fx avg `0.1095` n `6`; index avg `1.2524` n `23`; metal avg `1.7122` n `18`; unknown avg `1.0465` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
