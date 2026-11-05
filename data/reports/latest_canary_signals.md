# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T04:52:30.362873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `13`; crypto_alt avg `-0.1248` n `239`; crypto_major avg `-0.1128` n `8`; equity avg `-0.0371` n `158`; fx avg `-0.0079` n `6`; index avg `-0.0209` n `27`; metal avg `0.0083` n `20`; unknown avg `-0.053` n `1265`
- 1h: commodity avg `0.0469` n `13`; crypto_alt avg `-0.3297` n `239`; crypto_major avg `-0.0759` n `8`; equity avg `-0.2488` n `158`; fx avg `-0.0126` n `6`; index avg `-0.0615` n `27`; metal avg `-0.0192` n `20`; unknown avg `-0.0659` n `1241`
- 4h: commodity avg `-0.2341` n `13`; crypto_alt avg `0.1534` n `239`; crypto_major avg `-0.2747` n `8`; equity avg `-0.5706` n `158`; fx avg `0.0495` n `6`; index avg `-0.1729` n `27`; metal avg `0.2708` n `20`; unknown avg `-0.162` n `1238`
- 24h: commodity avg `-1.7336` n `13`; crypto_alt avg `2.8902` n `239`; crypto_major avg `3.2888` n `8`; equity avg `-0.1527` n `158`; fx avg `0.1051` n `6`; index avg `0.2106` n `27`; metal avg `1.7437` n `20`; unknown avg `33.2037` n `1020`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2536`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1915`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1885`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
