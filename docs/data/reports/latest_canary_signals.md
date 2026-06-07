# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T05:37:22.775008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0459` n `12`; crypto_alt avg `0.3674` n `228`; crypto_major avg `0.1188` n `8`; equity avg `0.0186` n `74`; fx avg `0.0` n `6`; index avg `-0.0176` n `23`; metal avg `-0.0092` n `18`; unknown avg `-0.3591` n `516`
- 1h: commodity avg `-0.0689` n `12`; crypto_alt avg `0.5644` n `228`; crypto_major avg `0.6965` n `8`; equity avg `0.3027` n `74`; fx avg `0.0051` n `6`; index avg `0.0656` n `23`; metal avg `0.123` n `18`; unknown avg `-0.477` n `516`
- 4h: commodity avg `-0.144` n `12`; crypto_alt avg `0.1083` n `228`; crypto_major avg `0.8842` n `8`; equity avg `0.4561` n `74`; fx avg `0.0088` n `6`; index avg `0.2938` n `23`; metal avg `0.3418` n `18`; unknown avg `-0.2844` n `516`
- 24h: commodity avg `0.1448` n `12`; crypto_alt avg `3.7734` n `228`; crypto_major avg `2.5154` n `8`; equity avg `2.0697` n `74`; fx avg `0.0563` n `6`; index avg `1.179` n `23`; metal avg `0.7635` n `18`; unknown avg `0.6074` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
