# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T09:22:22.115177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3146` n `12`; crypto_alt avg `0.2724` n `228`; crypto_major avg `0.2902` n `8`; equity avg `0.1233` n `69`; fx avg `-0.0009` n `6`; index avg `0.0676` n `23`; metal avg `0.16` n `18`; unknown avg `0.1821` n `417`
- 1h: commodity avg `-0.5352` n `12`; crypto_alt avg `0.1507` n `228`; crypto_major avg `0.0932` n `8`; equity avg `0.0179` n `69`; fx avg `-0.0207` n `6`; index avg `0.0583` n `23`; metal avg `0.1612` n `18`; unknown avg `0.1012` n `417`
- 4h: commodity avg `-0.0318` n `12`; crypto_alt avg `0.7293` n `228`; crypto_major avg `0.6557` n `8`; equity avg `-0.0667` n `69`; fx avg `-0.0136` n `6`; index avg `0.0448` n `23`; metal avg `-0.1081` n `18`; unknown avg `1.2387` n `407`
- 24h: commodity avg `0.1981` n `12`; crypto_alt avg `1.9688` n `228`; crypto_major avg `2.4824` n `8`; equity avg `3.455` n `69`; fx avg `0.1282` n `6`; index avg `1.3085` n `23`; metal avg `1.6484` n `18`; unknown avg `1.9691` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
