# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T11:52:39.877373+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0614` n `13`; crypto_alt avg `0.0758` n `239`; crypto_major avg `-0.0761` n `8`; equity avg `-0.0825` n `162`; fx avg `-0.0022` n `6`; index avg `-0.0091` n `27`; metal avg `0.0252` n `20`; unknown avg `158.3253` n `1265`
- 1h: commodity avg `-0.089` n `13`; crypto_alt avg `0.3633` n `239`; crypto_major avg `0.14` n `8`; equity avg `0.0718` n `162`; fx avg `-0.0003` n `6`; index avg `0.0096` n `27`; metal avg `0.1126` n `20`; unknown avg `0.2098` n `1263`
- 4h: commodity avg `-0.1958` n `13`; crypto_alt avg `-0.0598` n `239`; crypto_major avg `-0.1557` n `8`; equity avg `-0.419` n `162`; fx avg `-0.0195` n `6`; index avg `-0.0231` n `27`; metal avg `0.195` n `20`; unknown avg `31.4343` n `1219`
- 24h: commodity avg `-0.4675` n `13`; crypto_alt avg `-1.0138` n `239`; crypto_major avg `-1.0216` n `8`; equity avg `-0.9839` n `162`; fx avg `-0.0534` n `6`; index avg `-0.071` n `27`; metal avg `0.1371` n `20`; unknown avg `35.0761` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1343`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1147`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1107`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1003`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.094`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0702`, n `669`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0665`, n `669`, weak_sample_signal
