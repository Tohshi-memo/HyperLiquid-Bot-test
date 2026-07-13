# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T04:52:24.262269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3052` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0191` n `12`; crypto_alt avg `0.1763` n `230`; crypto_major avg `0.023` n `8`; equity avg `0.0224` n `92`; fx avg `0.0081` n `6`; index avg `0.0007` n `25`; metal avg `0.0072` n `20`; unknown avg `0.0991` n `766`
- 1h: commodity avg `0.037` n `12`; crypto_alt avg `0.3469` n `230`; crypto_major avg `-0.0797` n `8`; equity avg `-0.2542` n `92`; fx avg `0.0048` n `6`; index avg `-0.0639` n `25`; metal avg `0.0004` n `20`; unknown avg `-0.1888` n `766`
- 4h: commodity avg `0.0022` n `12`; crypto_alt avg `-1.279` n `230`; crypto_major avg `-1.649` n `8`; equity avg `-1.6273` n `92`; fx avg `0.0537` n `6`; index avg `-0.3438` n `25`; metal avg `-0.2202` n `20`; unknown avg `3.1908` n `766`
- 24h: commodity avg `0.1213` n `12`; crypto_alt avg `-1.8812` n `230`; crypto_major avg `-1.3013` n `8`; equity avg `-2.4839` n `92`; fx avg `0.0493` n `6`; index avg `-0.543` n `25`; metal avg `-0.4977` n `20`; unknown avg `-0.124` n `741`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
