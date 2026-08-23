# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T06:37:29.818183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3979` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0076` n `12`; crypto_alt avg `0.2618` n `230`; crypto_major avg `0.1342` n `8`; equity avg `0.0295` n `121`; fx avg `0.0221` n `6`; index avg `-0.0022` n `25`; metal avg `-0.0042` n `20`; unknown avg `-0.0106` n `794`
- 1h: commodity avg `0.0341` n `12`; crypto_alt avg `0.3775` n `230`; crypto_major avg `0.083` n `8`; equity avg `-0.0489` n `121`; fx avg `0.0409` n `6`; index avg `-0.0215` n `25`; metal avg `-0.0173` n `20`; unknown avg `0.279` n `778`
- 4h: commodity avg `-0.017` n `12`; crypto_alt avg `-1.3951` n `230`; crypto_major avg `-1.4282` n `8`; equity avg `-0.2203` n `121`; fx avg `0.0359` n `6`; index avg `-0.0303` n `25`; metal avg `-0.0326` n `20`; unknown avg `0.2426` n `778`
- 24h: commodity avg `-0.0083` n `12`; crypto_alt avg `-3.8246` n `230`; crypto_major avg `-2.329` n `8`; equity avg `-0.0477` n `121`; fx avg `0.1194` n `6`; index avg `-0.0199` n `25`; metal avg `0.0748` n `20`; unknown avg `3.4383` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
