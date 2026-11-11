# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T20:07:30.053301+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0283` n `13`; crypto_alt avg `0.0982` n `239`; crypto_major avg `0.0539` n `8`; equity avg `-0.1446` n `161`; fx avg `0.0069` n `6`; index avg `-0.0129` n `27`; metal avg `-0.0283` n `20`; unknown avg `3.5693` n `1250`
- 1h: commodity avg `-0.2156` n `13`; crypto_alt avg `0.1087` n `239`; crypto_major avg `0.0555` n `8`; equity avg `-0.3702` n `161`; fx avg `0.003` n `6`; index avg `-0.0312` n `27`; metal avg `-0.0173` n `20`; unknown avg `30.7582` n `1248`
- 4h: commodity avg `-0.4674` n `13`; crypto_alt avg `-0.6882` n `239`; crypto_major avg `-0.0554` n `8`; equity avg `-0.3202` n `161`; fx avg `-0.0022` n `6`; index avg `0.0239` n `27`; metal avg `-0.2598` n `20`; unknown avg `4.3446` n `1247`
- 24h: commodity avg `0.1368` n `13`; crypto_alt avg `0.8573` n `239`; crypto_major avg `1.3481` n `8`; equity avg `5.6076` n `161`; fx avg `-0.1419` n `6`; index avg `0.5548` n `27`; metal avg `0.007` n `20`; unknown avg `10.1857` n `1155`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
