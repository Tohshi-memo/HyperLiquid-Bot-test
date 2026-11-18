# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T17:52:33.035292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0476` n `13`; crypto_alt avg `-0.3525` n `239`; crypto_major avg `-0.4134` n `8`; equity avg `-0.211` n `164`; fx avg `0.0034` n `6`; index avg `-0.024` n `27`; metal avg `-0.0687` n `20`; unknown avg `1.1651` n `1265`
- 1h: commodity avg `-0.0748` n `13`; crypto_alt avg `0.7479` n `239`; crypto_major avg `1.0846` n `8`; equity avg `1.149` n `164`; fx avg `0.0161` n `6`; index avg `0.115` n `27`; metal avg `0.0234` n `20`; unknown avg `2.7843` n `1263`
- 4h: commodity avg `-0.3894` n `13`; crypto_alt avg `-0.9577` n `239`; crypto_major avg `-1.0333` n `8`; equity avg `-1.1521` n `164`; fx avg `-0.0325` n `6`; index avg `-0.0917` n `27`; metal avg `-0.3232` n `20`; unknown avg `0.8923` n `1257`
- 24h: commodity avg `-0.463` n `13`; crypto_alt avg `0.2986` n `239`; crypto_major avg `-0.314` n `8`; equity avg `0.6359` n `164`; fx avg `-0.1842` n `6`; index avg `0.0807` n `27`; metal avg `-1.2306` n `20`; unknown avg `-0.0025` n `1138`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0447`, n `668`, weak_sample_signal
