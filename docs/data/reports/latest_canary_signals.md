# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T14:57:53.336351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1353` n `13`; crypto_alt avg `0.1281` n `239`; crypto_major avg `-0.0337` n `8`; equity avg `0.76` n `158`; fx avg `-0.0207` n `6`; index avg `0.0605` n `27`; metal avg `0.1227` n `20`; unknown avg `1.3233` n `1255`
- 1h: commodity avg `-0.1594` n `13`; crypto_alt avg `0.4314` n `239`; crypto_major avg `-0.1168` n `8`; equity avg `-0.1011` n `158`; fx avg `0.0282` n `6`; index avg `0.0264` n `27`; metal avg `0.0947` n `20`; unknown avg `112.8965` n `1253`
- 4h: commodity avg `-0.2552` n `13`; crypto_alt avg `0.6426` n `239`; crypto_major avg `-0.137` n `8`; equity avg `0.4182` n `158`; fx avg `0.0251` n `6`; index avg `0.0915` n `27`; metal avg `0.0648` n `20`; unknown avg `97.227` n `1177`
- 24h: commodity avg `0.2663` n `13`; crypto_alt avg `-0.4945` n `239`; crypto_major avg `-3.281` n `8`; equity avg `-0.1158` n `158`; fx avg `-0.0435` n `6`; index avg `-0.1812` n `27`; metal avg `-0.2986` n `20`; unknown avg `57.1683` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
