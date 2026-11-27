# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T10:22:35.474120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0579` n `13`; crypto_alt avg `-0.1643` n `239`; crypto_major avg `-0.0215` n `8`; equity avg `0.208` n `168`; fx avg `-0.0002` n `6`; index avg `0.0227` n `27`; metal avg `0.0274` n `20`; unknown avg `-0.131` n `1261`
- 1h: commodity avg `0.0716` n `13`; crypto_alt avg `-0.1564` n `239`; crypto_major avg `0.0867` n `8`; equity avg `-0.4763` n `168`; fx avg `0.0229` n `6`; index avg `-0.0485` n `27`; metal avg `-0.0938` n `20`; unknown avg `159.8846` n `1253`
- 4h: commodity avg `-0.2416` n `13`; crypto_alt avg `-0.1881` n `239`; crypto_major avg `0.0912` n `8`; equity avg `-0.1518` n `168`; fx avg `-0.0794` n `6`; index avg `-0.0398` n `27`; metal avg `0.0874` n `20`; unknown avg `181.93` n `1121`
- 24h: commodity avg `0.3609` n `13`; crypto_alt avg `1.8269` n `239`; crypto_major avg `2.6712` n `8`; equity avg `4.0027` n `168`; fx avg `-0.1048` n `6`; index avg `0.3142` n `27`; metal avg `1.246` n `20`; unknown avg `73.5869` n `1029`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
