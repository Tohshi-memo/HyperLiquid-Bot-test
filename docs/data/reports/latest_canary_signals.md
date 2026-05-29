# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T08:52:19.452850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0311` n `12`; crypto_alt avg `0.0059` n `228`; crypto_major avg `-0.0515` n `8`; equity avg `-0.1106` n `69`; fx avg `-0.0251` n `6`; index avg `-0.0857` n `23`; metal avg `-0.1015` n `18`; unknown avg `-0.0403` n `417`
- 1h: commodity avg `0.1519` n `12`; crypto_alt avg `0.1847` n `228`; crypto_major avg `0.2265` n `8`; equity avg `-0.1841` n `69`; fx avg `-0.0277` n `6`; index avg `-0.0866` n `23`; metal avg `-0.4526` n `18`; unknown avg `-0.0103` n `417`
- 4h: commodity avg `0.5789` n `12`; crypto_alt avg `0.5122` n `228`; crypto_major avg `0.6182` n `8`; equity avg `-0.1319` n `69`; fx avg `0.0119` n `6`; index avg `-0.0462` n `23`; metal avg `-0.4246` n `18`; unknown avg `1.1826` n `407`
- 24h: commodity avg `0.8083` n `12`; crypto_alt avg `1.4687` n `228`; crypto_major avg `2.2521` n `8`; equity avg `3.3319` n `69`; fx avg `0.1255` n `6`; index avg `1.1527` n `23`; metal avg `1.4342` n `18`; unknown avg `1.8701` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
