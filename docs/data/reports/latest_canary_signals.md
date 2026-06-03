# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T12:52:25.160541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0485` n `12`; crypto_alt avg `0.0342` n `228`; crypto_major avg `0.0281` n `8`; equity avg `0.1468` n `72`; fx avg `-0.0356` n `6`; index avg `0.0051` n `23`; metal avg `0.3201` n `18`; unknown avg `-0.0496` n `420`
- 1h: commodity avg `0.0019` n `12`; crypto_alt avg `0.3104` n `228`; crypto_major avg `0.2412` n `8`; equity avg `-0.0372` n `72`; fx avg `-0.0551` n `6`; index avg `-0.1211` n `23`; metal avg `-0.1941` n `18`; unknown avg `-0.0406` n `420`
- 4h: commodity avg `-0.1331` n `12`; crypto_alt avg `0.3916` n `228`; crypto_major avg `0.0075` n `8`; equity avg `-0.1163` n `72`; fx avg `-0.0058` n `6`; index avg `-0.049` n `23`; metal avg `0.0858` n `18`; unknown avg `-0.7299` n `420`
- 24h: commodity avg `1.8737` n `12`; crypto_alt avg `-0.9493` n `228`; crypto_major avg `-3.2565` n `8`; equity avg `0.4251` n `72`; fx avg `0.0088` n `6`; index avg `0.6923` n `23`; metal avg `-1.5262` n `18`; unknown avg `-0.4182` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0455`, n `668`, weak_sample_signal
