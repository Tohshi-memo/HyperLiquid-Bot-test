# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T03:52:23.099070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0287` n `13`; crypto_alt avg `0.1047` n `239`; crypto_major avg `0.2318` n `8`; equity avg `0.0201` n `168`; fx avg `-0.0137` n `6`; index avg `-0.0018` n `27`; metal avg `0.0231` n `20`; unknown avg `2.794` n `1267`
- 1h: commodity avg `0.1549` n `13`; crypto_alt avg `0.0069` n `239`; crypto_major avg `0.1443` n `8`; equity avg `0.0704` n `168`; fx avg `0.0097` n `6`; index avg `0.0112` n `27`; metal avg `-0.0848` n `20`; unknown avg `2.0338` n `1261`
- 4h: commodity avg `0.121` n `13`; crypto_alt avg `1.0651` n `239`; crypto_major avg `0.9427` n `8`; equity avg `0.8887` n `168`; fx avg `-0.0472` n `6`; index avg `0.0791` n `27`; metal avg `0.1546` n `20`; unknown avg `0.9422` n `1247`
- 24h: commodity avg `0.7759` n `13`; crypto_alt avg `3.9794` n `239`; crypto_major avg `3.0536` n `8`; equity avg `2.205` n `168`; fx avg `0.0188` n `6`; index avg `0.1796` n `27`; metal avg `0.5799` n `20`; unknown avg `770.6566` n `1017`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.2017`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
