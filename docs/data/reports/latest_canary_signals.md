# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T04:07:25.415132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0486` n `13`; crypto_alt avg `-0.3394` n `239`; crypto_major avg `-0.2568` n `8`; equity avg `-0.1183` n `158`; fx avg `0.0102` n `6`; index avg `-0.0229` n `27`; metal avg `0.0246` n `20`; unknown avg `-0.2239` n `1247`
- 1h: commodity avg `-0.0991` n `13`; crypto_alt avg `-0.111` n `239`; crypto_major avg `-0.2641` n `8`; equity avg `-0.3182` n `158`; fx avg `0.015` n `6`; index avg `-0.0876` n `27`; metal avg `0.0131` n `20`; unknown avg `-0.2096` n `1245`
- 4h: commodity avg `-0.3237` n `13`; crypto_alt avg `0.3936` n `239`; crypto_major avg `-0.0854` n `8`; equity avg `-0.6` n `158`; fx avg `0.0411` n `6`; index avg `-0.1816` n `27`; metal avg `0.5161` n `20`; unknown avg `-0.1223` n `1244`
- 24h: commodity avg `-1.7385` n `13`; crypto_alt avg `3.7012` n `239`; crypto_major avg `3.663` n `8`; equity avg `0.8665` n `158`; fx avg `0.167` n `6`; index avg `0.4046` n `27`; metal avg `1.9445` n `20`; unknown avg `34.4094` n `1026`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2511`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1979`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1954`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
