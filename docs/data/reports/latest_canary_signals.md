# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T12:22:27.530263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `12`; crypto_alt avg `-0.2165` n `234`; crypto_major avg `-0.1603` n `8`; equity avg `0.0017` n `140`; fx avg `-0.0189` n `6`; index avg `-0.0046` n `26`; metal avg `0.0108` n `20`; unknown avg `0.6729` n `943`
- 1h: commodity avg `0.0237` n `12`; crypto_alt avg `0.3603` n `234`; crypto_major avg `0.3102` n `8`; equity avg `0.0461` n `140`; fx avg `-0.0186` n `6`; index avg `0.008` n `26`; metal avg `0.0041` n `20`; unknown avg `0.7603` n `935`
- 4h: commodity avg `0.022` n `12`; crypto_alt avg `-0.2322` n `234`; crypto_major avg `0.094` n `8`; equity avg `-0.0153` n `140`; fx avg `-0.0047` n `6`; index avg `0.009` n `26`; metal avg `-0.0146` n `20`; unknown avg `0.8782` n `935`
- 24h: commodity avg `0.2805` n `12`; crypto_alt avg `-2.2398` n `234`; crypto_major avg `-2.1609` n `8`; equity avg `-0.2534` n `140`; fx avg `-0.0505` n `6`; index avg `-0.0532` n `26`; metal avg `-0.0177` n `20`; unknown avg `0.861` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
