# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T01:07:30.743808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0106` n `12`; crypto_alt avg `0.0452` n `230`; crypto_major avg `0.0595` n `8`; equity avg `0.0342` n `102`; fx avg `0.0` n `6`; index avg `0.0052` n `25`; metal avg `-0.0053` n `20`; unknown avg `0.236` n `781`
- 1h: commodity avg `-0.0841` n `12`; crypto_alt avg `0.3837` n `230`; crypto_major avg `0.1759` n `8`; equity avg `-0.1242` n `102`; fx avg `-0.0013` n `6`; index avg `-0.0344` n `25`; metal avg `-0.0057` n `20`; unknown avg `0.1808` n `781`
- 4h: commodity avg `0.0914` n `12`; crypto_alt avg `0.5431` n `230`; crypto_major avg `0.1025` n `8`; equity avg `-0.1765` n `102`; fx avg `0.0125` n `6`; index avg `-0.0062` n `25`; metal avg `-0.0136` n `20`; unknown avg `3.7684` n `781`
- 24h: commodity avg `0.9452` n `12`; crypto_alt avg `-0.4817` n `230`; crypto_major avg `-2.2311` n `8`; equity avg `-2.8736` n `102`; fx avg `-0.1186` n `6`; index avg `-0.4189` n `25`; metal avg `-0.3206` n `20`; unknown avg `2.6417` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
