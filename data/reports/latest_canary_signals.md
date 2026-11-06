# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T23:37:27.443975+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0225` n `13`; crypto_alt avg `0.0274` n `239`; crypto_major avg `0.1042` n `8`; equity avg `-0.0771` n `158`; fx avg `0.0036` n `6`; index avg `-0.0048` n `27`; metal avg `-0.0181` n `20`; unknown avg `7.2613` n `1261`
- 1h: commodity avg `-0.0036` n `13`; crypto_alt avg `-0.2405` n `239`; crypto_major avg `-0.1128` n `8`; equity avg `-0.1947` n `158`; fx avg `0.0076` n `6`; index avg `-0.0064` n `27`; metal avg `-0.0132` n `20`; unknown avg `4.9866` n `1239`
- 4h: commodity avg `-0.0356` n `13`; crypto_alt avg `-0.3238` n `239`; crypto_major avg `0.045` n `8`; equity avg `0.2825` n `158`; fx avg `0.0112` n `6`; index avg `-0.0272` n `27`; metal avg `0.0419` n `20`; unknown avg `-0.1614` n `1165`
- 24h: commodity avg `0.0291` n `13`; crypto_alt avg `2.1126` n `239`; crypto_major avg `0.464` n `8`; equity avg `3.9706` n `158`; fx avg `-0.053` n `6`; index avg `0.4829` n `27`; metal avg `0.0365` n `20`; unknown avg `9.1364` n `1022`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
