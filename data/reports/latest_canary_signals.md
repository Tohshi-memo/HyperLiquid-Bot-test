# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T08:37:21.080270+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0861` n `12`; crypto_alt avg `-0.3149` n `228`; crypto_major avg `-0.1381` n `8`; equity avg `-0.0471` n `69`; fx avg `0.017` n `6`; index avg `0.0153` n `23`; metal avg `-0.1` n `18`; unknown avg `0.0051` n `417`
- 1h: commodity avg `0.1443` n `12`; crypto_alt avg `0.1725` n `228`; crypto_major avg `0.366` n `8`; equity avg `-0.0103` n `69`; fx avg `-0.008` n `6`; index avg `0.0312` n `23`; metal avg `-0.2829` n `18`; unknown avg `0.1083` n `417`
- 4h: commodity avg `0.5143` n `12`; crypto_alt avg `0.4686` n `228`; crypto_major avg `0.6535` n `8`; equity avg `0.028` n `69`; fx avg `0.0563` n `6`; index avg `0.0222` n `23`; metal avg `-0.322` n `18`; unknown avg `1.3055` n `407`
- 24h: commodity avg `0.7412` n `12`; crypto_alt avg `1.3937` n `228`; crypto_major avg `2.3152` n `8`; equity avg `3.4226` n `69`; fx avg `0.1664` n `6`; index avg `1.251` n `23`; metal avg `1.4991` n `18`; unknown avg `1.9547` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
