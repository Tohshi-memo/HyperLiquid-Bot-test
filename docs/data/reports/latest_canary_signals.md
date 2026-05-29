# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T11:58:35.832655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0319` n `12`; crypto_alt avg `-0.2675` n `228`; crypto_major avg `-0.1381` n `8`; equity avg `0.0829` n `69`; fx avg `0.002` n `6`; index avg `0.0003` n `23`; metal avg `0.127` n `18`; unknown avg `-0.0175` n `417`
- 1h: commodity avg `0.1741` n `12`; crypto_alt avg `-0.4814` n `228`; crypto_major avg `-0.3739` n `8`; equity avg `-0.1181` n `69`; fx avg `-0.0083` n `6`; index avg `0.088` n `23`; metal avg `-0.0408` n `18`; unknown avg `0.8237` n `417`
- 4h: commodity avg `-0.3105` n `12`; crypto_alt avg `-0.3265` n `228`; crypto_major avg `-0.2048` n `8`; equity avg `-0.2543` n `69`; fx avg `-0.0277` n `6`; index avg `0.1396` n `23`; metal avg `0.1068` n `18`; unknown avg `-0.1727` n `417`
- 24h: commodity avg `-0.1807` n `12`; crypto_alt avg `1.3495` n `228`; crypto_major avg `1.7989` n `8`; equity avg `3.4395` n `69`; fx avg `0.1356` n `6`; index avg `1.5517` n `23`; metal avg `2.545` n `18`; unknown avg `1.8431` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
