# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T06:37:16.113723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0338` n `12`; crypto_alt avg `0.1863` n `228`; crypto_major avg `0.0661` n `8`; equity avg `0.07` n `69`; fx avg `0.0` n `6`; index avg `0.0221` n `23`; metal avg `0.0029` n `18`; unknown avg `-0.1447` n `421`
- 1h: commodity avg `-0.0059` n `12`; crypto_alt avg `0.1784` n `228`; crypto_major avg `0.1322` n `8`; equity avg `0.036` n `69`; fx avg `0.0047` n `6`; index avg `0.0727` n `23`; metal avg `0.0159` n `18`; unknown avg `-0.1727` n `401`
- 4h: commodity avg `-0.0335` n `12`; crypto_alt avg `-0.1939` n `228`; crypto_major avg `0.103` n `8`; equity avg `0.178` n `69`; fx avg `0.0056` n `6`; index avg `0.0972` n `23`; metal avg `-0.0174` n `18`; unknown avg `0.1` n `401`
- 24h: commodity avg `-0.1895` n `12`; crypto_alt avg `1.8685` n `228`; crypto_major avg `2.0343` n `8`; equity avg `0.8438` n `69`; fx avg `0.0439` n `6`; index avg `0.0912` n `23`; metal avg `0.0085` n `18`; unknown avg `0.78` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1915`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
