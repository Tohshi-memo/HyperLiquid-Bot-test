# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T02:22:27.616338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0378` n `13`; crypto_alt avg `-0.154` n `239`; crypto_major avg `-0.2826` n `8`; equity avg `-0.1867` n `162`; fx avg `0.0161` n `6`; index avg `-0.0344` n `27`; metal avg `-0.0238` n `20`; unknown avg `0.324` n `1264`
- 1h: commodity avg `-0.0991` n `13`; crypto_alt avg `0.2341` n `239`; crypto_major avg `0.0099` n `8`; equity avg `-0.1451` n `162`; fx avg `-0.0017` n `6`; index avg `-0.0362` n `27`; metal avg `0.1418` n `20`; unknown avg `0.5769` n `1264`
- 4h: commodity avg `-0.151` n `13`; crypto_alt avg `-0.5353` n `239`; crypto_major avg `-0.764` n `8`; equity avg `-0.037` n `162`; fx avg `0.0487` n `6`; index avg `-0.002` n `27`; metal avg `0.1457` n `20`; unknown avg `6.7097` n `1226`
- 24h: commodity avg `-1.0368` n `13`; crypto_alt avg `-0.5962` n `239`; crypto_major avg `-0.2113` n `8`; equity avg `-3.4713` n `162`; fx avg `-0.0462` n `6`; index avg `-0.3566` n `27`; metal avg `-0.2206` n `20`; unknown avg `560.2816` n `999`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
