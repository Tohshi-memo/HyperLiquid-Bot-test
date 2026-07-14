# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T03:52:23.112012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.062` n `12`; crypto_alt avg `0.1088` n `230`; crypto_major avg `0.064` n `8`; equity avg `0.2065` n `92`; fx avg `-0.0016` n `6`; index avg `0.0656` n `25`; metal avg `0.0139` n `20`; unknown avg `-0.0581` n `766`
- 1h: commodity avg `0.0125` n `12`; crypto_alt avg `-0.0183` n `230`; crypto_major avg `-0.0692` n `8`; equity avg `-0.0508` n `92`; fx avg `-0.0524` n `6`; index avg `-0.0044` n `25`; metal avg `0.0625` n `20`; unknown avg `-0.1784` n `766`
- 4h: commodity avg `-0.0117` n `12`; crypto_alt avg `0.1703` n `230`; crypto_major avg `0.0923` n `8`; equity avg `0.0802` n `92`; fx avg `-0.0962` n `6`; index avg `-0.0304` n `25`; metal avg `0.1292` n `20`; unknown avg `-0.2589` n `766`
- 24h: commodity avg `1.0043` n `12`; crypto_alt avg `-0.2746` n `230`; crypto_major avg `-0.8498` n `8`; equity avg `-1.6188` n `92`; fx avg `-0.2321` n `6`; index avg `-0.3026` n `25`; metal avg `0.0141` n `20`; unknown avg `-0.2663` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1963`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
