# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T12:14:56.988251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1155` n `12`; crypto_alt avg `0.0685` n `228`; crypto_major avg `-0.0014` n `8`; equity avg `0.0584` n `69`; fx avg `0.0005` n `6`; index avg `0.0022` n `23`; metal avg `-0.013` n `18`; unknown avg `1.1181` n `421`
- 1h: commodity avg `0.122` n `12`; crypto_alt avg `0.044` n `228`; crypto_major avg `0.1529` n `8`; equity avg `0.0791` n `69`; fx avg `0.0009` n `6`; index avg `0.0032` n `23`; metal avg `-0.0318` n `18`; unknown avg `0.8981` n `421`
- 4h: commodity avg `0.1969` n `12`; crypto_alt avg `0.0701` n `228`; crypto_major avg `0.2849` n `8`; equity avg `0.1569` n `69`; fx avg `0.0209` n `6`; index avg `-0.054` n `23`; metal avg `0.0154` n `18`; unknown avg `0.8705` n `421`
- 24h: commodity avg `-0.1378` n `12`; crypto_alt avg `2.2338` n `228`; crypto_major avg `2.6427` n `8`; equity avg `1.4442` n `69`; fx avg `0.1113` n `6`; index avg `-0.0056` n `23`; metal avg `-0.0219` n `18`; unknown avg `0.8295` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1921`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
