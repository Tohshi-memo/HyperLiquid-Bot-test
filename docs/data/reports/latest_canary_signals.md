# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T16:22:31.899502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0448` n `13`; crypto_alt avg `0.1484` n `239`; crypto_major avg `-0.0997` n `8`; equity avg `0.2277` n `162`; fx avg `0.0112` n `6`; index avg `0.0113` n `27`; metal avg `0.022` n `20`; unknown avg `1.3412` n `1261`
- 1h: commodity avg `-0.0849` n `13`; crypto_alt avg `1.3292` n `239`; crypto_major avg `0.9542` n `8`; equity avg `1.8987` n `162`; fx avg `0.0135` n `6`; index avg `0.1681` n `27`; metal avg `0.2062` n `20`; unknown avg `5.5252` n `1245`
- 4h: commodity avg `0.2618` n `13`; crypto_alt avg `0.2029` n `239`; crypto_major avg `-0.3556` n `8`; equity avg `1.0524` n `162`; fx avg `-0.01` n `6`; index avg `0.1641` n `27`; metal avg `-0.3628` n `20`; unknown avg `3.1626` n `1241`
- 24h: commodity avg `-0.1719` n `13`; crypto_alt avg `-3.1524` n `239`; crypto_major avg `-3.1461` n `8`; equity avg `-1.8658` n `162`; fx avg `-0.1355` n `6`; index avg `-0.0392` n `27`; metal avg `-0.9491` n `20`; unknown avg `3.1603` n `1149`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
