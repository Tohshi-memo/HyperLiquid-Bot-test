# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T10:22:29.531219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0052` n `13`; crypto_alt avg `-0.3802` n `236`; crypto_major avg `-0.2933` n `8`; equity avg `0.095` n `151`; fx avg `-0.0224` n `6`; index avg `0.0191` n `26`; metal avg `-0.043` n `20`; unknown avg `0.0204` n `1112`
- 1h: commodity avg `-0.0449` n `13`; crypto_alt avg `-0.5588` n `236`; crypto_major avg `-0.3953` n `8`; equity avg `-0.1789` n `151`; fx avg `-0.0454` n `6`; index avg `-0.0149` n `26`; metal avg `0.0047` n `20`; unknown avg `-0.227` n `1078`
- 4h: commodity avg `-0.0167` n `13`; crypto_alt avg `0.2277` n `236`; crypto_major avg `0.2063` n `8`; equity avg `-0.3462` n `151`; fx avg `-0.043` n `6`; index avg `-0.0208` n `26`; metal avg `0.2399` n `20`; unknown avg `4.3527` n `1062`
- 24h: commodity avg `-0.4716` n `13`; crypto_alt avg `-4.6133` n `236`; crypto_major avg `-3.4232` n `8`; equity avg `-5.9098` n `151`; fx avg `0.0394` n `6`; index avg `-0.9578` n `26`; metal avg `-0.4277` n `20`; unknown avg `2.2524` n `970`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1207`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1047`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0875`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0842`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0788`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0702`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
