# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T10:58:12.767401+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `0.0312` n `230`; crypto_major avg `0.0296` n `8`; equity avg `-0.0022` n `114`; fx avg `0.0` n `6`; index avg `0.0013` n `25`; metal avg `0.0029` n `20`; unknown avg `-0.0196` n `791`
- 1h: commodity avg `-0.0112` n `12`; crypto_alt avg `-0.0489` n `230`; crypto_major avg `-0.0458` n `8`; equity avg `-0.0287` n `114`; fx avg `-0.0003` n `6`; index avg `-0.011` n `25`; metal avg `0.0075` n `20`; unknown avg `0.1162` n `791`
- 4h: commodity avg `0.0116` n `12`; crypto_alt avg `0.3702` n `230`; crypto_major avg `0.0661` n `8`; equity avg `-0.022` n `114`; fx avg `0.002` n `6`; index avg `-0.0051` n `25`; metal avg `0.0048` n `20`; unknown avg `0.1305` n `791`
- 24h: commodity avg `0.1227` n `12`; crypto_alt avg `0.1019` n `230`; crypto_major avg `0.1177` n `8`; equity avg `0.3795` n `114`; fx avg `-0.036` n `6`; index avg `0.05` n `25`; metal avg `0.0337` n `20`; unknown avg `0.1916` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2085`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
