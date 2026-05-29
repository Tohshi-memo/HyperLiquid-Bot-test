# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T06:22:21.241757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1772` n `12`; crypto_alt avg `0.2807` n `228`; crypto_major avg `0.2996` n `8`; equity avg `0.069` n `69`; fx avg `0.026` n `6`; index avg `0.0511` n `23`; metal avg `0.0078` n `18`; unknown avg `-0.0391` n `417`
- 1h: commodity avg `-0.0976` n `12`; crypto_alt avg `0.4976` n `228`; crypto_major avg `0.3571` n `8`; equity avg `0.0235` n `69`; fx avg `0.0269` n `6`; index avg `0.0871` n `23`; metal avg `0.0083` n `18`; unknown avg `0.0697` n `407`
- 4h: commodity avg `-0.1689` n `12`; crypto_alt avg `0.3092` n `228`; crypto_major avg `0.6441` n `8`; equity avg `0.5834` n `69`; fx avg `0.0498` n `6`; index avg `0.2455` n `23`; metal avg `0.0126` n `18`; unknown avg `-0.0322` n `407`
- 24h: commodity avg `-0.146` n `12`; crypto_alt avg `1.8956` n `228`; crypto_major avg `2.4203` n `8`; equity avg `3.8666` n `69`; fx avg `0.1848` n `6`; index avg `1.4326` n `23`; metal avg `2.2069` n `18`; unknown avg `0.8773` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
