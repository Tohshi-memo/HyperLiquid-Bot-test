# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T14:23:37.298615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0396` n `13`; crypto_alt avg `0.3757` n `239`; crypto_major avg `0.536` n `8`; equity avg `0.0967` n `162`; fx avg `-0.0084` n `6`; index avg `0.0025` n `27`; metal avg `-0.046` n `20`; unknown avg `0.2887` n `1253`
- 1h: commodity avg `-0.148` n `13`; crypto_alt avg `0.8558` n `239`; crypto_major avg `0.7145` n `8`; equity avg `0.2685` n `162`; fx avg `-0.0105` n `6`; index avg `0.0307` n `27`; metal avg `-0.0801` n `20`; unknown avg `13.2238` n `1251`
- 4h: commodity avg `-0.4167` n `13`; crypto_alt avg `0.0083` n `239`; crypto_major avg `0.0325` n `8`; equity avg `-0.4922` n `162`; fx avg `0.0056` n `6`; index avg `-0.0568` n `27`; metal avg `-0.0487` n `20`; unknown avg `13.1438` n `1245`
- 24h: commodity avg `-0.626` n `13`; crypto_alt avg `-0.8624` n `239`; crypto_major avg `-0.9734` n `8`; equity avg `-1.3739` n `162`; fx avg `-0.0184` n `6`; index avg `-0.112` n `27`; metal avg `-0.0816` n `20`; unknown avg `49.0713` n `1044`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1371`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1143`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1087`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.108`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1051`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1028`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0884`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0861`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0836`, n `669`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0753`, n `669`, weak_sample_signal
