# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T09:07:32.959432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0149` n `13`; crypto_alt avg `-0.2364` n `239`; crypto_major avg `-0.4147` n `8`; equity avg `-0.48` n `165`; fx avg `-0.0082` n `6`; index avg `-0.0391` n `27`; metal avg `-0.1117` n `20`; unknown avg `-0.1491` n `1246`
- 1h: commodity avg `-0.3025` n `13`; crypto_alt avg `-0.2487` n `239`; crypto_major avg `-0.5709` n `8`; equity avg `-0.5054` n `165`; fx avg `-0.0508` n `6`; index avg `-0.0356` n `27`; metal avg `-0.0013` n `20`; unknown avg `3.2317` n `1242`
- 4h: commodity avg `-0.4762` n `13`; crypto_alt avg `0.7563` n `239`; crypto_major avg `0.3904` n `8`; equity avg `-0.1212` n `165`; fx avg `-0.0408` n `6`; index avg `0.0429` n `27`; metal avg `0.4597` n `20`; unknown avg `0.762` n `1176`
- 24h: commodity avg `-0.4836` n `13`; crypto_alt avg `-3.4619` n `239`; crypto_major avg `-3.2021` n `8`; equity avg `-7.3675` n `165`; fx avg `-0.1249` n `6`; index avg `-0.6633` n `27`; metal avg `-1.4561` n `20`; unknown avg `4.4299` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
