# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T01:11:25.220043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `12`; crypto_alt avg `-0.0602` n `230`; crypto_major avg `0.0159` n `8`; equity avg `0.0411` n `100`; fx avg `0.0012` n `6`; index avg `0.0106` n `25`; metal avg `0.0019` n `20`; unknown avg `-0.0181` n `774`
- 1h: commodity avg `-0.0123` n `12`; crypto_alt avg `-0.0069` n `230`; crypto_major avg `0.0469` n `8`; equity avg `0.0038` n `100`; fx avg `-0.0013` n `6`; index avg `-0.0068` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.1109` n `774`
- 4h: commodity avg `-0.05` n `12`; crypto_alt avg `0.03` n `230`; crypto_major avg `0.1239` n `8`; equity avg `0.1163` n `100`; fx avg `-0.005` n `6`; index avg `0.0246` n `25`; metal avg `0.0003` n `20`; unknown avg `-0.2723` n `774`
- 24h: commodity avg `-0.597` n `12`; crypto_alt avg `0.2088` n `230`; crypto_major avg `1.0089` n `8`; equity avg `0.4554` n `100`; fx avg `-0.0468` n `6`; index avg `0.1302` n `25`; metal avg `0.015` n `20`; unknown avg `-0.2626` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.135`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1235`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.122`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1168`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1167`, n `666`, weak_sample_signal
