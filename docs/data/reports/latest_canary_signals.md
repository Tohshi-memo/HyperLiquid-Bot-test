# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T19:43:20.272143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0279` n `12`; crypto_alt avg `-0.0208` n `230`; crypto_major avg `-0.0899` n `8`; equity avg `-0.0081` n `121`; fx avg `-0.0041` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0276` n `20`; unknown avg `0.2665` n `793`
- 1h: commodity avg `-0.0912` n `12`; crypto_alt avg `-0.9915` n `230`; crypto_major avg `-0.4803` n `8`; equity avg `0.115` n `121`; fx avg `-0.0016` n `6`; index avg `0.0063` n `25`; metal avg `-0.0307` n `20`; unknown avg `1.1505` n `793`
- 4h: commodity avg `-0.0763` n `12`; crypto_alt avg `-0.873` n `230`; crypto_major avg `-0.6673` n `8`; equity avg `-0.0555` n `121`; fx avg `0.0297` n `6`; index avg `-0.0383` n `25`; metal avg `0.0242` n `20`; unknown avg `1.3981` n `793`
- 24h: commodity avg `0.0807` n `12`; crypto_alt avg `6.5384` n `230`; crypto_major avg `4.7064` n `8`; equity avg `1.0226` n `121`; fx avg `-0.0949` n `6`; index avg `0.1022` n `25`; metal avg `0.5315` n `20`; unknown avg `2.2035` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
