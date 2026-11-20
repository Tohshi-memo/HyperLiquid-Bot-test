# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T09:52:26.467672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0386` n `13`; crypto_alt avg `-0.0404` n `239`; crypto_major avg `0.14` n `8`; equity avg `-0.1775` n `165`; fx avg `0.0077` n `6`; index avg `-0.0323` n `27`; metal avg `-0.0393` n `20`; unknown avg `158.2739` n `1262`
- 1h: commodity avg `-0.1215` n `13`; crypto_alt avg `-0.3081` n `239`; crypto_major avg `-0.4478` n `8`; equity avg `-1.1258` n `165`; fx avg `0.0335` n `6`; index avg `-0.1226` n `27`; metal avg `-0.1505` n `20`; unknown avg `3.4386` n `1246`
- 4h: commodity avg `-0.5002` n `13`; crypto_alt avg `-0.2494` n `239`; crypto_major avg `-0.5915` n `8`; equity avg `-0.979` n `165`; fx avg `-0.0165` n `6`; index avg `-0.057` n `27`; metal avg `0.2096` n `20`; unknown avg `3.4658` n `1176`
- 24h: commodity avg `-0.5809` n `13`; crypto_alt avg `-3.5387` n `239`; crypto_major avg `-3.2108` n `8`; equity avg `-8.0065` n `165`; fx avg `-0.0758` n `6`; index avg `-0.8361` n `27`; metal avg `-1.4648` n `20`; unknown avg `17.1778` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
