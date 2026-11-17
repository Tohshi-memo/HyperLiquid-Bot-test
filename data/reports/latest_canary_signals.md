# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T10:37:38.418918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0168` n `13`; crypto_alt avg `-0.0987` n `239`; crypto_major avg `-0.0861` n `8`; equity avg `0.0029` n `162`; fx avg `0.0113` n `6`; index avg `0.0171` n `27`; metal avg `0.055` n `20`; unknown avg `0.313` n `1266`
- 1h: commodity avg `-0.072` n `13`; crypto_alt avg `-0.0192` n `239`; crypto_major avg `-0.1964` n `8`; equity avg `0.2907` n `162`; fx avg `-0.009` n `6`; index avg `0.0613` n `27`; metal avg `0.0053` n `20`; unknown avg `252.967` n `1264`
- 4h: commodity avg `0.1589` n `13`; crypto_alt avg `-0.2132` n `239`; crypto_major avg `-0.3204` n `8`; equity avg `-0.4336` n `162`; fx avg `-0.0588` n `6`; index avg `-0.0133` n `27`; metal avg `-0.1401` n `20`; unknown avg `142.6463` n `1190`
- 24h: commodity avg `-0.8346` n `13`; crypto_alt avg `0.4403` n `239`; crypto_major avg `0.3169` n `8`; equity avg `-2.9596` n `162`; fx avg `-0.0664` n `6`; index avg `-0.2833` n `27`; metal avg `-0.2014` n `20`; unknown avg `11.0866` n `1115`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
