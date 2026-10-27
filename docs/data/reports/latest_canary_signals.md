# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T01:52:28.748050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0243` n `13`; crypto_alt avg `-0.0961` n `237`; crypto_major avg `-0.1459` n `8`; equity avg `0.0001` n `154`; fx avg `-0.0099` n `6`; index avg `-0.0094` n `27`; metal avg `-0.0838` n `20`; unknown avg `0.088` n `1238`
- 1h: commodity avg `-0.065` n `13`; crypto_alt avg `-0.3118` n `237`; crypto_major avg `-0.3288` n `8`; equity avg `-0.1697` n `154`; fx avg `-0.0143` n `6`; index avg `-0.0164` n `27`; metal avg `-0.0536` n `20`; unknown avg `0.7557` n `1234`
- 4h: commodity avg `-0.0864` n `13`; crypto_alt avg `-0.0289` n `237`; crypto_major avg `0.2575` n `8`; equity avg `0.3745` n `154`; fx avg `-0.0118` n `6`; index avg `0.13` n `27`; metal avg `-0.0838` n `20`; unknown avg `0.9022` n `1210`
- 24h: commodity avg `-0.0224` n `13`; crypto_alt avg `0.6556` n `237`; crypto_major avg `0.9098` n `8`; equity avg `2.0748` n `153`; fx avg `-0.0409` n `6`; index avg `0.1235` n `27`; metal avg `0.0223` n `20`; unknown avg `998.1713` n `1004`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2228`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2025`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1991`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
