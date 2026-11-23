# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T22:07:37.511972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2963` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0404` n `13`; crypto_alt avg `-0.2002` n `239`; crypto_major avg `-0.0406` n `8`; equity avg `0.1216` n `166`; fx avg `-0.005` n `6`; index avg `0.0157` n `27`; metal avg `0.024` n `20`; unknown avg `207.4146` n `1252`
- 1h: commodity avg `0.0127` n `13`; crypto_alt avg `-0.4995` n `239`; crypto_major avg `-0.3838` n `8`; equity avg `0.0649` n `166`; fx avg `-0.0177` n `6`; index avg `0.0083` n `27`; metal avg `-0.0282` n `20`; unknown avg `202.7069` n `1244`
- 4h: commodity avg `-0.1938` n `13`; crypto_alt avg `-1.7699` n `239`; crypto_major avg `-1.2833` n `8`; equity avg `-0.0555` n `166`; fx avg `-0.0075` n `6`; index avg `0.013` n `27`; metal avg `-0.163` n `20`; unknown avg `1.8171` n `1220`
- 24h: commodity avg `-1.4208` n `13`; crypto_alt avg `0.7834` n `239`; crypto_major avg `1.2413` n `8`; equity avg `6.1432` n `166`; fx avg `-0.196` n `6`; index avg `0.5792` n `27`; metal avg `0.5878` n `20`; unknown avg `99.0872` n `1050`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
