# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T20:01:25.503626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.94` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0094` n `12`; crypto_alt avg `-0.0141` n `230`; crypto_major avg `-0.1353` n `8`; equity avg `0.0342` n `92`; fx avg `-0.0046` n `6`; index avg `-0.0159` n `25`; metal avg `0.0202` n `20`; unknown avg `0.0529` n `768`
- 1h: commodity avg `0.0345` n `12`; crypto_alt avg `0.031` n `230`; crypto_major avg `-0.064` n `8`; equity avg `0.2213` n `92`; fx avg `-0.0065` n `6`; index avg `0.0319` n `25`; metal avg `0.0438` n `20`; unknown avg `-0.0312` n `768`
- 4h: commodity avg `0.053` n `12`; crypto_alt avg `-0.3803` n `230`; crypto_major avg `-0.1027` n `8`; equity avg `0.3188` n `92`; fx avg `-0.0201` n `6`; index avg `0.0728` n `25`; metal avg `0.037` n `20`; unknown avg `-0.1442` n `766`
- 24h: commodity avg `0.3691` n `12`; crypto_alt avg `1.6` n `230`; crypto_major avg `3.1046` n `8`; equity avg `1.3328` n `92`; fx avg `-0.0243` n `6`; index avg `0.3635` n `25`; metal avg `0.5762` n `20`; unknown avg `0.0084` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1878`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
