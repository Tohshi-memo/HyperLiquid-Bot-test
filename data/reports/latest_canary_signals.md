# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T19:07:26.622225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.27` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `0.047` n `230`; crypto_major avg `0.0178` n `8`; equity avg `-0.1095` n `92`; fx avg `0.0097` n `6`; index avg `-0.0338` n `25`; metal avg `0.0068` n `20`; unknown avg `-0.1095` n `768`
- 1h: commodity avg `0.1234` n `12`; crypto_alt avg `-0.1506` n `230`; crypto_major avg `0.1539` n `8`; equity avg `-0.1743` n `92`; fx avg `0.0029` n `6`; index avg `-0.0527` n `25`; metal avg `-0.0598` n `20`; unknown avg `-0.0864` n `768`
- 4h: commodity avg `0.3576` n `12`; crypto_alt avg `-0.3271` n `230`; crypto_major avg `0.2368` n `8`; equity avg `-0.0021` n `92`; fx avg `-0.0312` n `6`; index avg `-0.0347` n `25`; metal avg `-0.3901` n `20`; unknown avg `-0.3276` n `766`
- 24h: commodity avg `0.3569` n `12`; crypto_alt avg `1.7901` n `230`; crypto_major avg `3.5068` n `8`; equity avg `1.1448` n `92`; fx avg `-0.0125` n `6`; index avg `0.3021` n `25`; metal avg `0.5744` n `20`; unknown avg `-0.0647` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
