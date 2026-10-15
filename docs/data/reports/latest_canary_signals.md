# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T12:37:40.632604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1949` n `13`; crypto_alt avg `-0.2652` n `236`; crypto_major avg `-0.2989` n `8`; equity avg `-0.1376` n `151`; fx avg `0.0028` n `6`; index avg `-0.0161` n `26`; metal avg `0.051` n `20`; unknown avg `0.7029` n `1136`
- 1h: commodity avg `-0.1685` n `13`; crypto_alt avg `-0.4586` n `236`; crypto_major avg `-0.5065` n `8`; equity avg `-0.497` n `151`; fx avg `0.0019` n `6`; index avg `-0.0582` n `26`; metal avg `-0.0332` n `20`; unknown avg `1.4653` n `1128`
- 4h: commodity avg `-0.1474` n `13`; crypto_alt avg `-0.8145` n `236`; crypto_major avg `-0.7969` n `8`; equity avg `-0.4064` n `151`; fx avg `0.0125` n `6`; index avg `-0.0316` n `26`; metal avg `0.0414` n `20`; unknown avg `0.1696` n `1048`
- 24h: commodity avg `-0.4068` n `13`; crypto_alt avg `-4.3298` n `236`; crypto_major avg `-3.2265` n `8`; equity avg `-5.39` n `151`; fx avg `0.1324` n `6`; index avg `-0.7947` n `26`; metal avg `-0.1832` n `20`; unknown avg `0.9045` n `957`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1209`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1032`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0987`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0849`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0803`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0719`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
