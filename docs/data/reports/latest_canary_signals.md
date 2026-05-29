# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T07:37:17.748651+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2209` n `12`; crypto_alt avg `-0.6344` n `228`; crypto_major avg `-0.4027` n `8`; equity avg `-0.1302` n `69`; fx avg `-0.0071` n `6`; index avg `-0.0038` n `23`; metal avg `0.0379` n `18`; unknown avg `0.8825` n `417`
- 1h: commodity avg `0.4614` n `12`; crypto_alt avg `-0.0742` n `228`; crypto_major avg `-0.0247` n `8`; equity avg `-0.1548` n `69`; fx avg `-0.0082` n `6`; index avg `-0.0445` n `23`; metal avg `0.0214` n `18`; unknown avg `1.2595` n `417`
- 4h: commodity avg `0.3956` n `12`; crypto_alt avg `0.349` n `228`; crypto_major avg `0.3096` n `8`; equity avg `0.3041` n `69`; fx avg `0.0536` n `6`; index avg `0.1446` n `23`; metal avg `0.2174` n `18`; unknown avg `0.9271` n `407`
- 24h: commodity avg `0.486` n `12`; crypto_alt avg `0.7194` n `228`; crypto_major avg `1.3887` n `8`; equity avg `3.6656` n `69`; fx avg `0.1519` n `6`; index avg `1.2596` n `23`; metal avg `1.7659` n `18`; unknown avg `1.5405` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
