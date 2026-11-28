# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T02:52:32.415498+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.011` n `13`; crypto_alt avg `-0.1656` n `239`; crypto_major avg `-0.0511` n `8`; equity avg `-0.0324` n `168`; fx avg `-0.0071` n `6`; index avg `-0.0074` n `27`; metal avg `-0.005` n `20`; unknown avg `0.4411` n `1265`
- 1h: commodity avg `0.0486` n `13`; crypto_alt avg `-0.6681` n `239`; crypto_major avg `-0.427` n `8`; equity avg `0.0905` n `168`; fx avg `-0.0114` n `6`; index avg `0.002` n `27`; metal avg `0.0495` n `20`; unknown avg `0.6619` n `1257`
- 4h: commodity avg `-0.0616` n `13`; crypto_alt avg `-0.2975` n `239`; crypto_major avg `0.3898` n `8`; equity avg `0.2334` n `168`; fx avg `-0.0129` n `6`; index avg `0.032` n `27`; metal avg `0.0438` n `20`; unknown avg `1.7524` n `1239`
- 24h: commodity avg `-0.7309` n `13`; crypto_alt avg `-1.2835` n `239`; crypto_major avg `-1.1316` n `8`; equity avg `1.3519` n `168`; fx avg `-0.1966` n `6`; index avg `0.1304` n `27`; metal avg `0.1875` n `20`; unknown avg `282.9277` n `989`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
