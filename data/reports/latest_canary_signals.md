# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T22:07:33.790886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0163` n `13`; crypto_alt avg `-0.162` n `239`; crypto_major avg `-0.1486` n `8`; equity avg `-0.1505` n `166`; fx avg `0.0469` n `6`; index avg `-0.0134` n `27`; metal avg `-0.0146` n `20`; unknown avg `-0.0107` n `1248`
- 1h: commodity avg `-0.0684` n `13`; crypto_alt avg `-0.1782` n `239`; crypto_major avg `-0.2115` n `8`; equity avg `-0.0487` n `166`; fx avg `0.1016` n `6`; index avg `0.0253` n `27`; metal avg `-0.0027` n `20`; unknown avg `164.9669` n `1248`
- 4h: commodity avg `-0.046` n `13`; crypto_alt avg `-0.1663` n `239`; crypto_major avg `0.0116` n `8`; equity avg `-0.2144` n `166`; fx avg `0.1047` n `6`; index avg `-0.0154` n `27`; metal avg `-0.0854` n `20`; unknown avg `165.8828` n `1210`
- 24h: commodity avg `-0.1693` n `13`; crypto_alt avg `0.8758` n `239`; crypto_major avg `0.9069` n `8`; equity avg `0.8488` n `166`; fx avg `0.0904` n `6`; index avg `0.1189` n `27`; metal avg `0.0046` n `20`; unknown avg `235.7171` n `1058`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
