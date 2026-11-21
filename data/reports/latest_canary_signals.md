# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T19:52:29.411594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `13`; crypto_alt avg `0.0945` n `239`; crypto_major avg `-0.0194` n `8`; equity avg `-0.0125` n `166`; fx avg `0.0005` n `6`; index avg `-0.0002` n `27`; metal avg `0.0192` n `20`; unknown avg `212.2779` n `1262`
- 1h: commodity avg `0.0319` n `13`; crypto_alt avg `-0.1014` n `239`; crypto_major avg `0.2754` n `8`; equity avg `0.0326` n `166`; fx avg `-0.0015` n `6`; index avg `0.029` n `27`; metal avg `-0.0177` n `20`; unknown avg `40.6396` n `1248`
- 4h: commodity avg `0.0938` n `13`; crypto_alt avg `-0.3258` n `239`; crypto_major avg `0.5994` n `8`; equity avg `0.1467` n `166`; fx avg `0.0024` n `6`; index avg `0.0567` n `27`; metal avg `0.0827` n `20`; unknown avg `0.0053` n `1196`
- 24h: commodity avg `0.1892` n `13`; crypto_alt avg `1.2608` n `239`; crypto_major avg `3.116` n `8`; equity avg `1.3037` n `166`; fx avg `-0.0762` n `6`; index avg `0.2002` n `27`; metal avg `0.316` n `20`; unknown avg `0.3816` n `1088`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
