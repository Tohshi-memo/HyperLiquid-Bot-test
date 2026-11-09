# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T17:52:26.131773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.9005` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0223` n `13`; crypto_alt avg `0.0893` n `239`; crypto_major avg `0.0799` n `8`; equity avg `-0.0929` n `160`; fx avg `-0.0025` n `6`; index avg `-0.0103` n `27`; metal avg `-0.0233` n `20`; unknown avg `0.1031` n `1261`
- 1h: commodity avg `-0.0374` n `13`; crypto_alt avg `-0.2606` n `239`; crypto_major avg `-0.3221` n `8`; equity avg `-0.1816` n `160`; fx avg `0.0012` n `6`; index avg `0.0264` n `27`; metal avg `-0.022` n `20`; unknown avg `0.4391` n `1255`
- 4h: commodity avg `0.1343` n `13`; crypto_alt avg `0.0979` n `239`; crypto_major avg `0.3847` n `8`; equity avg `3.2852` n `160`; fx avg `-0.0021` n `6`; index avg `0.3627` n `27`; metal avg `-0.084` n `20`; unknown avg `4.7584` n `1249`
- 24h: commodity avg `-0.3335` n `13`; crypto_alt avg `0.759` n `239`; crypto_major avg `-2.378` n `8`; equity avg `3.877` n `160`; fx avg `-0.1574` n `6`; index avg `0.457` n `27`; metal avg `0.3495` n `20`; unknown avg `6.7911` n `1026`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
