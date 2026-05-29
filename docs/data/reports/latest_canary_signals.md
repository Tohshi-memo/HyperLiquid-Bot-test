# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T07:07:16.745347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.028` n `12`; crypto_alt avg `0.0615` n `228`; crypto_major avg `0.0543` n `8`; equity avg `-0.0133` n `69`; fx avg `0.0023` n `6`; index avg `-0.0249` n `23`; metal avg `0.0596` n `18`; unknown avg `0.2438` n `417`
- 1h: commodity avg `-0.0902` n `12`; crypto_alt avg `0.2946` n `228`; crypto_major avg `0.2685` n `8`; equity avg `0.1684` n `69`; fx avg `0.0487` n `6`; index avg `-0.0111` n `23`; metal avg `0.0724` n `18`; unknown avg `0.1138` n `417`
- 4h: commodity avg `0.0046` n `12`; crypto_alt avg `0.6234` n `228`; crypto_major avg `0.5228` n `8`; equity avg `0.6537` n `69`; fx avg `0.0753` n `6`; index avg `0.1916` n `23`; metal avg `0.2576` n `18`; unknown avg `0.2178` n `407`
- 24h: commodity avg `0.0703` n `12`; crypto_alt avg `1.7692` n `228`; crypto_major avg `2.1974` n `8`; equity avg `3.9235` n `69`; fx avg `0.1762` n `6`; index avg `1.2562` n `23`; metal avg `1.8972` n `18`; unknown avg `0.8804` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.172`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
