# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T08:07:21.636926+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.165` n `12`; crypto_alt avg `0.2282` n `228`; crypto_major avg `0.2792` n `8`; equity avg `0.0153` n `69`; fx avg `-0.0106` n `6`; index avg `-0.0287` n `23`; metal avg `-0.1652` n `18`; unknown avg `0.0809` n `417`
- 1h: commodity avg `0.6516` n `12`; crypto_alt avg `-0.2016` n `228`; crypto_major avg `0.0973` n `8`; equity avg `-0.1428` n `69`; fx avg `-0.0335` n `6`; index avg `-0.0499` n `23`; metal avg `-0.2544` n `18`; unknown avg `1.131` n `417`
- 4h: commodity avg `0.4933` n `12`; crypto_alt avg `0.8806` n `228`; crypto_major avg `0.8454` n `8`; equity avg `0.3571` n `69`; fx avg `0.0423` n `6`; index avg `0.0798` n `23`; metal avg `0.0391` n `18`; unknown avg `1.2816` n `407`
- 24h: commodity avg `0.7384` n `12`; crypto_alt avg `1.0511` n `228`; crypto_major avg `1.8486` n `8`; equity avg `3.6175` n `69`; fx avg `0.1492` n `6`; index avg `1.1916` n `23`; metal avg `1.5663` n `18`; unknown avg `1.6948` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
