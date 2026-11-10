# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T08:07:33.314202+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0382` n `13`; crypto_alt avg `-0.1045` n `239`; crypto_major avg `-0.2975` n `8`; equity avg `0.1794` n `160`; fx avg `-0.0008` n `6`; index avg `0.0175` n `27`; metal avg `0.0308` n `20`; unknown avg `0.116` n `1241`
- 1h: commodity avg `-0.0591` n `13`; crypto_alt avg `-0.1835` n `239`; crypto_major avg `-0.2547` n `8`; equity avg `0.3317` n `160`; fx avg `-0.0124` n `6`; index avg `0.0296` n `27`; metal avg `-0.0486` n `20`; unknown avg `-0.0293` n `1239`
- 4h: commodity avg `-0.1469` n `13`; crypto_alt avg `0.2912` n `239`; crypto_major avg `0.1634` n `8`; equity avg `0.713` n `160`; fx avg `-0.0807` n `6`; index avg `0.1092` n `27`; metal avg `-0.0538` n `20`; unknown avg `1.8509` n `1211`
- 24h: commodity avg `-0.5326` n `13`; crypto_alt avg `2.9128` n `239`; crypto_major avg `1.3672` n `8`; equity avg `5.6478` n `160`; fx avg `-0.0036` n `6`; index avg `0.6419` n `27`; metal avg `0.2583` n `20`; unknown avg `182.0359` n `1129`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
