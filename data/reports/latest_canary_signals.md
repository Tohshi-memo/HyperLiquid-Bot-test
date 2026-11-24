# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T18:22:34.485392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0318` n `13`; crypto_alt avg `-0.1574` n `239`; crypto_major avg `-0.0357` n `8`; equity avg `0.028` n `168`; fx avg `-0.0079` n `6`; index avg `0.005` n `27`; metal avg `-0.0491` n `20`; unknown avg `0.0351` n `1263`
- 1h: commodity avg `0.0541` n `13`; crypto_alt avg `0.3124` n `239`; crypto_major avg `0.5593` n `8`; equity avg `0.4105` n `168`; fx avg `-0.0054` n `6`; index avg `0.0438` n `27`; metal avg `-0.0031` n `20`; unknown avg `166.8433` n `1249`
- 4h: commodity avg `0.1472` n `13`; crypto_alt avg `-0.54` n `239`; crypto_major avg `-0.5686` n `8`; equity avg `-1.3294` n `168`; fx avg `0.0157` n `6`; index avg `-0.0055` n `27`; metal avg `-0.5604` n `20`; unknown avg `371.8216` n `1245`
- 24h: commodity avg `0.5008` n `13`; crypto_alt avg `-3.7011` n `239`; crypto_major avg `-3.2145` n `8`; equity avg `-4.181` n `167`; fx avg `0.2627` n `6`; index avg `-0.2458` n `27`; metal avg `-1.2116` n `20`; unknown avg `177.7916` n `1129`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
