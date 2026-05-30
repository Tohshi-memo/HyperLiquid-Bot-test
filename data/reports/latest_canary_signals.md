# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T14:07:22.863352+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0488` n `12`; crypto_alt avg `0.2166` n `228`; crypto_major avg `0.1444` n `8`; equity avg `0.0464` n `69`; fx avg `0.0152` n `6`; index avg `0.0094` n `23`; metal avg `0.0094` n `18`; unknown avg `0.8158` n `421`
- 1h: commodity avg `0.1179` n `12`; crypto_alt avg `-0.0245` n `228`; crypto_major avg `0.114` n `8`; equity avg `0.1195` n `69`; fx avg `0.0` n `6`; index avg `-0.0029` n `23`; metal avg `-0.0033` n `18`; unknown avg `-0.0633` n `421`
- 4h: commodity avg `0.3523` n `12`; crypto_alt avg `0.2293` n `228`; crypto_major avg `0.4739` n `8`; equity avg `0.3391` n `69`; fx avg `0.0165` n `6`; index avg `0.0936` n `23`; metal avg `-0.0322` n `18`; unknown avg `0.7828` n `421`
- 24h: commodity avg `-0.2915` n `12`; crypto_alt avg `2.7127` n `228`; crypto_major avg `3.2974` n `8`; equity avg `1.4747` n `69`; fx avg `0.1018` n `6`; index avg `0.0751` n `23`; metal avg `-0.2577` n `18`; unknown avg `1.5015` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1919`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
