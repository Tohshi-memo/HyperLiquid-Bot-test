# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T01:52:26.112063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1162` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0586` n `12`; crypto_alt avg `0.1335` n `230`; crypto_major avg `0.1023` n `8`; equity avg `0.0244` n `92`; fx avg `0.0025` n `6`; index avg `0.0125` n `25`; metal avg `0.0048` n `20`; unknown avg `0.0991` n `765`
- 1h: commodity avg `-0.0212` n `12`; crypto_alt avg `0.7582` n `230`; crypto_major avg `0.6355` n `8`; equity avg `0.0541` n `92`; fx avg `0.0024` n `6`; index avg `0.0017` n `25`; metal avg `0.0118` n `20`; unknown avg `0.2938` n `765`
- 4h: commodity avg `0.5116` n `12`; crypto_alt avg `-1.2702` n `230`; crypto_major avg `-1.2397` n `8`; equity avg `-0.2181` n `92`; fx avg `0.0137` n `6`; index avg `-0.1235` n `25`; metal avg `-0.0343` n `20`; unknown avg `0.6095` n `765`
- 24h: commodity avg `0.5663` n `12`; crypto_alt avg `-0.5671` n `229`; crypto_major avg `-0.2272` n `8`; equity avg `0.1639` n `92`; fx avg `0.0201` n `6`; index avg `-0.0732` n `25`; metal avg `-0.065` n `20`; unknown avg `-0.4048` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1768`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
