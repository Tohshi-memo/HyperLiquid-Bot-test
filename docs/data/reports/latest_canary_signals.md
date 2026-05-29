# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T10:52:20.095803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.022` n `12`; crypto_alt avg `-0.0751` n `228`; crypto_major avg `-0.1733` n `8`; equity avg `-0.053` n `69`; fx avg `0.0045` n `6`; index avg `0.0287` n `23`; metal avg `-0.0308` n `18`; unknown avg `-0.0144` n `417`
- 1h: commodity avg `0.0028` n `12`; crypto_alt avg `-0.4032` n `228`; crypto_major avg `-0.2357` n `8`; equity avg `-0.0896` n `69`; fx avg `0.0097` n `6`; index avg `0.0391` n `23`; metal avg `0.0734` n `18`; unknown avg `-0.0518` n `417`
- 4h: commodity avg `-0.0316` n `12`; crypto_alt avg `-0.2082` n `228`; crypto_major avg `0.0412` n `8`; equity avg `-0.3028` n `69`; fx avg `-0.04` n `6`; index avg `0.0056` n `23`; metal avg `0.1174` n `18`; unknown avg `0.1405` n `417`
- 24h: commodity avg `0.0241` n `12`; crypto_alt avg `1.7688` n `228`; crypto_major avg `2.2289` n `8`; equity avg `3.6352` n `69`; fx avg `0.177` n `6`; index avg `1.5176` n `23`; metal avg `2.3345` n `18`; unknown avg `0.8239` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
