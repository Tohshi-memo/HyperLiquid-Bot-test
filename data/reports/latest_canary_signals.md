# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T10:37:18.652894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1745` n `12`; crypto_alt avg `-0.0516` n `228`; crypto_major avg `0.0654` n `8`; equity avg `0.078` n `69`; fx avg `0.005` n `6`; index avg `0.0573` n `23`; metal avg `0.2469` n `18`; unknown avg `-0.0016` n `417`
- 1h: commodity avg `-0.0032` n `12`; crypto_alt avg `-0.4261` n `228`; crypto_major avg `-0.1387` n `8`; equity avg `-0.0673` n `69`; fx avg `0.014` n `6`; index avg `-0.0003` n `23`; metal avg `0.2257` n `18`; unknown avg `-0.3641` n `417`
- 4h: commodity avg `-0.0267` n `12`; crypto_alt avg `0.1578` n `228`; crypto_major avg `0.407` n `8`; equity avg `-0.1735` n `69`; fx avg `-0.0375` n `6`; index avg `0.0109` n `23`; metal avg `0.2692` n `18`; unknown avg `0.2648` n `417`
- 24h: commodity avg `0.194` n `12`; crypto_alt avg `1.472` n `228`; crypto_major avg `2.1588` n `8`; equity avg `3.6102` n `69`; fx avg `0.162` n `6`; index avg `1.4138` n `23`; metal avg `2.2037` n `18`; unknown avg `0.8837` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
