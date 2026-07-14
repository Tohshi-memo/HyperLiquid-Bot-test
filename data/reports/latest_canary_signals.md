# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T22:26:42.495947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0319` n `12`; crypto_alt avg `0.2158` n `230`; crypto_major avg `0.2899` n `8`; equity avg `-0.0009` n `92`; fx avg `0.0083` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0239` n `20`; unknown avg `-0.1805` n `768`
- 1h: commodity avg `0.0406` n `12`; crypto_alt avg `0.1597` n `230`; crypto_major avg `0.0858` n `8`; equity avg `-0.0297` n `92`; fx avg `0.0119` n `6`; index avg `-0.0145` n `25`; metal avg `-0.0275` n `20`; unknown avg `2.192` n `768`
- 4h: commodity avg `0.178` n `12`; crypto_alt avg `0.2442` n `230`; crypto_major avg `0.4696` n `8`; equity avg `0.0029` n `92`; fx avg `0.0117` n `6`; index avg `-0.0449` n `25`; metal avg `-0.0412` n `20`; unknown avg `-0.2184` n `768`
- 24h: commodity avg `0.335` n `12`; crypto_alt avg `2.3093` n `230`; crypto_major avg `3.702` n `8`; equity avg `1.3239` n `92`; fx avg `0.0003` n `6`; index avg `0.3881` n `25`; metal avg `0.5269` n `20`; unknown avg `0.2096` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
