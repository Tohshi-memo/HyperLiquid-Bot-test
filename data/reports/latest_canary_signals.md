# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T07:37:24.728688+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0095` n `13`; crypto_alt avg `-0.085` n `239`; crypto_major avg `-0.155` n `8`; equity avg `-0.0876` n `162`; fx avg `0.001` n `6`; index avg `-0.0101` n `27`; metal avg `-0.0363` n `20`; unknown avg `0.6315` n `1262`
- 1h: commodity avg `-0.0364` n `13`; crypto_alt avg `0.8186` n `239`; crypto_major avg `0.3696` n `8`; equity avg `0.2509` n `162`; fx avg `0.013` n `6`; index avg `0.0341` n `27`; metal avg `-0.0047` n `20`; unknown avg `0.3837` n `1260`
- 4h: commodity avg `0.0191` n `13`; crypto_alt avg `1.5206` n `239`; crypto_major avg `0.3596` n `8`; equity avg `-0.3467` n `162`; fx avg `0.0485` n `6`; index avg `-0.0368` n `27`; metal avg `-0.2713` n `20`; unknown avg `2.4018` n `1218`
- 24h: commodity avg `0.591` n `13`; crypto_alt avg `-0.6647` n `239`; crypto_major avg `-3.0809` n `8`; equity avg `-1.0277` n `162`; fx avg `-0.0159` n `6`; index avg `0.0449` n `27`; metal avg `-0.5125` n `20`; unknown avg `98.7728` n `1133`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
