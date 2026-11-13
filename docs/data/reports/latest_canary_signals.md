# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T12:49:01.049973+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0438` n `13`; crypto_alt avg `-0.0091` n `239`; crypto_major avg `0.0546` n `8`; equity avg `-0.1412` n `162`; fx avg `-0.016` n `6`; index avg `-0.0179` n `27`; metal avg `-0.0268` n `20`; unknown avg `29.5093` n `1260`
- 1h: commodity avg `0.0993` n `13`; crypto_alt avg `0.2858` n `239`; crypto_major avg `0.1613` n `8`; equity avg `-0.4204` n `162`; fx avg `-0.0187` n `6`; index avg `-0.0435` n `27`; metal avg `-0.0579` n `20`; unknown avg `40.1987` n `1252`
- 4h: commodity avg `-0.0146` n `13`; crypto_alt avg `0.5033` n `239`; crypto_major avg `0.9106` n `8`; equity avg `0.4153` n `162`; fx avg `-0.0345` n `6`; index avg `0.059` n `27`; metal avg `0.0326` n `20`; unknown avg `41.8537` n `1198`
- 24h: commodity avg `0.9012` n `13`; crypto_alt avg `0.3589` n `239`; crypto_major avg `-1.4038` n `8`; equity avg `-0.4253` n `162`; fx avg `-0.0172` n `6`; index avg `0.0465` n `27`; metal avg `-0.2982` n `20`; unknown avg `0.5899` n `1073`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
