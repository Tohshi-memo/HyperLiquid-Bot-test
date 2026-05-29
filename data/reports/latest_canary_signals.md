# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T06:07:20.454043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0213` n `12`; crypto_alt avg `0.1406` n `228`; crypto_major avg `0.0166` n `8`; equity avg `0.0734` n `69`; fx avg `0.0023` n `6`; index avg `0.0461` n `23`; metal avg `0.1799` n `18`; unknown avg `0.0455` n `407`
- 1h: commodity avg `0.0217` n `12`; crypto_alt avg `0.0795` n `228`; crypto_major avg `0.004` n `8`; equity avg `-0.0161` n `69`; fx avg `0.0111` n `6`; index avg `0.0` n `23`; metal avg `0.0023` n `18`; unknown avg `0.0267` n `407`
- 4h: commodity avg `0.0691` n `12`; crypto_alt avg `-0.1945` n `228`; crypto_major avg `0.0082` n `8`; equity avg `0.4993` n `69`; fx avg `0.0256` n `6`; index avg `0.2125` n `23`; metal avg `0.0281` n `18`; unknown avg `-0.1325` n `407`
- 24h: commodity avg `0.0995` n `12`; crypto_alt avg `1.602` n `228`; crypto_major avg `2.1098` n `8`; equity avg `3.9167` n `69`; fx avg `0.1579` n `6`; index avg `1.4166` n `23`; metal avg `2.1557` n `18`; unknown avg `0.859` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
