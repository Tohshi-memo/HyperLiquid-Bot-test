# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T03:37:18.125676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0134` n `12`; crypto_alt avg `-0.2523` n `228`; crypto_major avg `-0.1236` n `8`; equity avg `-0.0508` n `69`; fx avg `0.0019` n `6`; index avg `-0.0179` n `23`; metal avg `-0.0046` n `18`; unknown avg `-0.0761` n `419`
- 1h: commodity avg `0.071` n `12`; crypto_alt avg `-0.3439` n `228`; crypto_major avg `-0.0914` n `8`; equity avg `-0.0099` n `69`; fx avg `0.0037` n `6`; index avg `-0.034` n `23`; metal avg `-0.0103` n `18`; unknown avg `-0.1499` n `419`
- 4h: commodity avg `-0.0676` n `12`; crypto_alt avg `1.404` n `228`; crypto_major avg `1.2827` n `8`; equity avg `0.2709` n `69`; fx avg `-0.0035` n `6`; index avg `-0.1322` n `23`; metal avg `0.0316` n `18`; unknown avg `-0.3566` n `419`
- 24h: commodity avg `-0.1514` n `12`; crypto_alt avg `2.1725` n `228`; crypto_major avg `2.1741` n `8`; equity avg `1.0912` n `69`; fx avg `0.1038` n `6`; index avg `0.1527` n `23`; metal avg `0.2115` n `18`; unknown avg `0.4649` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.187`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
