# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T17:22:25.159025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1122` n `13`; crypto_alt avg `0.0396` n `239`; crypto_major avg `0.0962` n `8`; equity avg `-0.2213` n `162`; fx avg `0.0034` n `6`; index avg `-0.0238` n `27`; metal avg `-0.0094` n `20`; unknown avg `5.668` n `1259`
- 1h: commodity avg `0.2081` n `13`; crypto_alt avg `-0.7632` n `239`; crypto_major avg `-0.3996` n `8`; equity avg `-1.0142` n `162`; fx avg `-0.0315` n `6`; index avg `-0.0973` n `27`; metal avg `-0.0512` n `20`; unknown avg `41.2941` n `1237`
- 4h: commodity avg `0.0886` n `13`; crypto_alt avg `-0.0231` n `239`; crypto_major avg `-0.1668` n `8`; equity avg `0.91` n `162`; fx avg `-0.0552` n `6`; index avg `0.1442` n `27`; metal avg `-0.2641` n `20`; unknown avg `44.3744` n `1227`
- 24h: commodity avg `0.2446` n `13`; crypto_alt avg `-4.3395` n `239`; crypto_major avg `-4.1052` n `8`; equity avg `-3.3295` n `162`; fx avg `-0.1244` n `6`; index avg `-0.191` n `27`; metal avg `-0.9604` n `20`; unknown avg `3.2118` n `1137`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
