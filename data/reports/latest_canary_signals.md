# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T15:22:32.407054+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `13`; crypto_alt avg `-0.0678` n `239`; crypto_major avg `0.0356` n `8`; equity avg `-0.0105` n `166`; fx avg `-0.0048` n `6`; index avg `-0.0189` n `27`; metal avg `-0.0041` n `20`; unknown avg `0.0141` n `1261`
- 1h: commodity avg `-0.013` n `13`; crypto_alt avg `-0.1207` n `239`; crypto_major avg `0.2547` n `8`; equity avg `0.0032` n `166`; fx avg `0.0022` n `6`; index avg `-0.0055` n `27`; metal avg `0.0305` n `20`; unknown avg `0.279` n `1253`
- 4h: commodity avg `-0.0433` n `13`; crypto_alt avg `-0.3689` n `239`; crypto_major avg `-0.1201` n `8`; equity avg `-0.0001` n `166`; fx avg `0.0093` n `6`; index avg `0.0432` n `27`; metal avg `0.0048` n `20`; unknown avg `150.49` n `1247`
- 24h: commodity avg `-0.0468` n `13`; crypto_alt avg `0.2494` n `239`; crypto_major avg `0.9085` n `8`; equity avg `1.0107` n `166`; fx avg `-0.0204` n `6`; index avg `0.1719` n `27`; metal avg `0.0316` n `20`; unknown avg `-0.0593` n `1078`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
