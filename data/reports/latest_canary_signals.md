# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T03:13:10.376882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0353` n `12`; crypto_alt avg `-0.2033` n `231`; crypto_major avg `-0.1733` n `8`; equity avg `-0.2237` n `122`; fx avg `0.0144` n `6`; index avg `-0.0297` n `25`; metal avg `0.033` n `20`; unknown avg `0.0749` n `793`
- 1h: commodity avg `0.0849` n `12`; crypto_alt avg `0.4102` n `231`; crypto_major avg `0.3523` n `8`; equity avg `-0.3256` n `122`; fx avg `0.0069` n `6`; index avg `0.0007` n `25`; metal avg `-0.0027` n `20`; unknown avg `-0.0994` n `793`
- 4h: commodity avg `-0.0781` n `12`; crypto_alt avg `-1.8971` n `231`; crypto_major avg `-1.1201` n `8`; equity avg `-1.4729` n `122`; fx avg `-0.0471` n `6`; index avg `-0.1279` n `25`; metal avg `0.0885` n `20`; unknown avg `0.7783` n `793`
- 24h: commodity avg `-0.2927` n `12`; crypto_alt avg `2.765` n `231`; crypto_major avg `0.4486` n `8`; equity avg `-0.9393` n `122`; fx avg `-0.1887` n `6`; index avg `-0.0551` n `25`; metal avg `0.0994` n `20`; unknown avg `5.9453` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
