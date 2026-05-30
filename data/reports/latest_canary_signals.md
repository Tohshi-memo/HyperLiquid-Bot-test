# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T11:07:19.749018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `12`; crypto_alt avg `-0.1192` n `228`; crypto_major avg `-0.1033` n `8`; equity avg `-0.0098` n `69`; fx avg `-0.0027` n `6`; index avg `0.0038` n `23`; metal avg `-0.0014` n `18`; unknown avg `-0.1247` n `421`
- 1h: commodity avg `0.0763` n `12`; crypto_alt avg `0.0103` n `228`; crypto_major avg `0.0592` n `8`; equity avg `0.0295` n `69`; fx avg `-0.0022` n `6`; index avg `0.0244` n `23`; metal avg `0.0103` n `18`; unknown avg `0.0058` n `421`
- 4h: commodity avg `0.048` n `12`; crypto_alt avg `0.168` n `228`; crypto_major avg `0.2802` n `8`; equity avg `0.1133` n `69`; fx avg `0.0205` n `6`; index avg `-0.0104` n `23`; metal avg `0.0331` n `18`; unknown avg `-0.1129` n `421`
- 24h: commodity avg `-0.2604` n `12`; crypto_alt avg `1.492` n `228`; crypto_major avg `1.9775` n `8`; equity avg `1.2221` n `69`; fx avg `0.1018` n `6`; index avg `-0.0209` n `23`; metal avg `-0.1253` n `18`; unknown avg `0.4832` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.192`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
