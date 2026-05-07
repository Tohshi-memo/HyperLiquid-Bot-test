# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T23:22:14.841902+00:00`
- Correlation status: `ready`
- Asset price records: `593`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1208` n `12`; crypto_alt avg `0.0094` n `228`; crypto_major avg `-0.0374` n `8`; equity avg `0.1223` n `65`; fx avg `0.0042` n `5`; index avg `0.0492` n `23`; metal avg `0.2116` n `18`; unknown avg `0.1283` n `365`
- 1h: commodity avg `0.1005` n `12`; crypto_alt avg `0.0457` n `228`; crypto_major avg `-0.0366` n `8`; equity avg `0.2699` n `65`; fx avg `-0.0176` n `5`; index avg `0.0388` n `23`; metal avg `0.0621` n `18`; unknown avg `0.0156` n `365`
- 4h: commodity avg `0.1921` n `12`; crypto_alt avg `0.2145` n `228`; crypto_major avg `-0.1331` n `8`; equity avg `-0.0515` n `65`; fx avg `-0.0383` n `5`; index avg `0.1034` n `23`; metal avg `-0.1376` n `18`; unknown avg `-0.2469` n `365`
- 24h: commodity avg `0.6999` n `12`; crypto_alt avg `1.479` n `228`; crypto_major avg `-1.828` n `8`; equity avg `-1.483` n `65`; fx avg `0.1346` n `5`; index avg `-0.7875` n `23`; metal avg `-0.1163` n `18`; unknown avg `-0.4429` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1394`, n `589`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1161`, n `589`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1107`, n `589`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1069`, n `589`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `585`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `585`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0869`, n `585`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0863`, n `585`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.081`, n `585`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0769`, n `585`, weak_sample_signal
