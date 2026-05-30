# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T10:22:18.158289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0174` n `12`; crypto_alt avg `0.1213` n `228`; crypto_major avg `0.0919` n `8`; equity avg `0.0189` n `69`; fx avg `-0.0109` n `6`; index avg `0.0053` n `23`; metal avg `0.0245` n `18`; unknown avg `0.1112` n `421`
- 1h: commodity avg `0.0277` n `12`; crypto_alt avg `0.1684` n `228`; crypto_major avg `0.1377` n `8`; equity avg `0.024` n `69`; fx avg `0.0065` n `6`; index avg `-0.0357` n `23`; metal avg `0.0475` n `18`; unknown avg `0.1864` n `421`
- 4h: commodity avg `-0.0025` n `12`; crypto_alt avg `0.0204` n `228`; crypto_major avg `0.2615` n `8`; equity avg `0.1419` n `69`; fx avg `0.0117` n `6`; index avg `-0.0244` n `23`; metal avg `0.0568` n `18`; unknown avg `-0.3317` n `421`
- 24h: commodity avg `-0.3734` n `12`; crypto_alt avg `1.4894` n `228`; crypto_major avg `1.8896` n `8`; equity avg `1.1853` n `69`; fx avg `0.0983` n `6`; index avg `0.0929` n `23`; metal avg `0.0401` n `18`; unknown avg `0.5012` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1918`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
