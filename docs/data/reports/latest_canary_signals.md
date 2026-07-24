# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T09:22:29.370423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.051` n `12`; crypto_alt avg `-0.1521` n `230`; crypto_major avg `-0.1556` n `8`; equity avg `0.0078` n `100`; fx avg `-0.0151` n `6`; index avg `0.0054` n `25`; metal avg `0.0026` n `20`; unknown avg `-0.0401` n `773`
- 1h: commodity avg `-0.2442` n `12`; crypto_alt avg `-0.2798` n `230`; crypto_major avg `-0.3568` n `8`; equity avg `0.1237` n `100`; fx avg `-0.0336` n `6`; index avg `0.0465` n `25`; metal avg `0.104` n `20`; unknown avg `-0.0204` n `772`
- 4h: commodity avg `-0.5134` n `12`; crypto_alt avg `-0.0883` n `230`; crypto_major avg `0.0161` n `8`; equity avg `0.1979` n `100`; fx avg `-0.0137` n `6`; index avg `0.0485` n `25`; metal avg `0.2543` n `20`; unknown avg `0.0015` n `756`
- 24h: commodity avg `-0.3403` n `12`; crypto_alt avg `-1.2855` n `230`; crypto_major avg `-1.7584` n `8`; equity avg `-1.9414` n `99`; fx avg `-0.152` n `6`; index avg `-0.4554` n `25`; metal avg `-0.3984` n `20`; unknown avg `0.0518` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0992`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0916`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0825`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0805`, n `666`, weak_sample_signal
