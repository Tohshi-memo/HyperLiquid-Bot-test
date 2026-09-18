# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T05:52:26.519847+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.03` n `12`; crypto_alt avg `-0.1732` n `234`; crypto_major avg `-0.2283` n `8`; equity avg `-0.0476` n `140`; fx avg `-0.0386` n `6`; index avg `-0.0127` n `26`; metal avg `0.0288` n `20`; unknown avg `9.9314` n `919`
- 1h: commodity avg `0.0029` n `12`; crypto_alt avg `-0.2526` n `234`; crypto_major avg `0.0273` n `8`; equity avg `0.046` n `140`; fx avg `-0.0512` n `6`; index avg `-0.0003` n `26`; metal avg `0.0787` n `20`; unknown avg `0.3296` n `917`
- 4h: commodity avg `-0.0135` n `12`; crypto_alt avg `1.352` n `234`; crypto_major avg `1.2263` n `8`; equity avg `0.8397` n `140`; fx avg `0.0513` n `6`; index avg `0.1386` n `26`; metal avg `0.237` n `20`; unknown avg `15.974` n `897`
- 24h: commodity avg `-0.2236` n `12`; crypto_alt avg `4.8661` n `234`; crypto_major avg `3.621` n `8`; equity avg `2.303` n `140`; fx avg `0.1312` n `6`; index avg `0.3642` n `26`; metal avg `0.5991` n `20`; unknown avg `4.7561` n `753`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
