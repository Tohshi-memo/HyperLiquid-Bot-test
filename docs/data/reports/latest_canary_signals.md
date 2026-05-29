# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T10:22:19.922359+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.107` n `12`; crypto_alt avg `-0.2356` n `228`; crypto_major avg `-0.0404` n `8`; equity avg `0.006` n `69`; fx avg `-0.0062` n `6`; index avg `0.0209` n `23`; metal avg `-0.0681` n `18`; unknown avg `-0.0155` n `417`
- 1h: commodity avg `0.1707` n `12`; crypto_alt avg `-0.3524` n `228`; crypto_major avg `-0.2303` n `8`; equity avg `-0.1499` n `69`; fx avg `0.0114` n `6`; index avg `-0.0757` n `23`; metal avg `0.0234` n `18`; unknown avg `-0.3755` n `417`
- 4h: commodity avg `0.2362` n `12`; crypto_alt avg `-0.1244` n `228`; crypto_major avg `0.0643` n `8`; equity avg `-0.2308` n `69`; fx avg `-0.0291` n `6`; index avg `-0.1177` n `23`; metal avg `-0.0933` n `18`; unknown avg `0.0823` n `417`
- 24h: commodity avg `0.4402` n `12`; crypto_alt avg `1.6343` n `228`; crypto_major avg `2.2221` n `8`; equity avg `3.517` n `69`; fx avg `0.1673` n `6`; index avg `1.3343` n `23`; metal avg `1.8081` n `18`; unknown avg `1.0211` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
