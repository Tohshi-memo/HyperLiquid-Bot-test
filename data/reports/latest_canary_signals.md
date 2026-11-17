# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T02:07:26.722675+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `13`; crypto_alt avg `0.0957` n `239`; crypto_major avg `-0.0032` n `8`; equity avg `0.0227` n `162`; fx avg `0.0005` n `6`; index avg `-0.007` n `27`; metal avg `0.0131` n `20`; unknown avg `-0.0518` n `1260`
- 1h: commodity avg `-0.0947` n `13`; crypto_alt avg `0.3363` n `239`; crypto_major avg `0.3295` n `8`; equity avg `0.1575` n `162`; fx avg `0.0034` n `6`; index avg `-0.0022` n `27`; metal avg `0.1587` n `20`; unknown avg `8.7045` n `1262`
- 4h: commodity avg `-0.0523` n `13`; crypto_alt avg `-0.4672` n `239`; crypto_major avg `-0.613` n `8`; equity avg `0.209` n `162`; fx avg `0.0352` n `6`; index avg `0.0449` n `27`; metal avg `0.1751` n `20`; unknown avg `1.9349` n `1226`
- 24h: commodity avg `-1.0196` n `13`; crypto_alt avg `0.1539` n `239`; crypto_major avg `0.4761` n `8`; equity avg `-3.1238` n `162`; fx avg `-0.0587` n `6`; index avg `-0.3108` n `27`; metal avg `-0.1832` n `20`; unknown avg `511.6755` n `997`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
