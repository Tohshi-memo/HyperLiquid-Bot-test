# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T23:22:28.941487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `-0.0206` n `230`; crypto_major avg `-0.0071` n `8`; equity avg `-0.0994` n `100`; fx avg `-0.0155` n `6`; index avg `-0.0041` n `25`; metal avg `-0.0058` n `20`; unknown avg `0.0558` n `774`
- 1h: commodity avg `0.0049` n `12`; crypto_alt avg `0.2826` n `230`; crypto_major avg `0.2424` n `8`; equity avg `-0.0849` n `100`; fx avg `0.0346` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0021` n `20`; unknown avg `0.1847` n `774`
- 4h: commodity avg `0.1908` n `12`; crypto_alt avg `-0.0994` n `230`; crypto_major avg `-0.1773` n `8`; equity avg `-0.0074` n `100`; fx avg `0.0202` n `6`; index avg `0.0069` n `25`; metal avg `0.0321` n `20`; unknown avg `-0.0186` n `773`
- 24h: commodity avg `-0.2931` n `12`; crypto_alt avg `-0.9838` n `230`; crypto_major avg `-1.1561` n `8`; equity avg `-3.3868` n `100`; fx avg `-0.1321` n `6`; index avg `-0.4745` n `25`; metal avg `0.0159` n `20`; unknown avg `14.0115` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1266`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1219`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1122`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1102`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
