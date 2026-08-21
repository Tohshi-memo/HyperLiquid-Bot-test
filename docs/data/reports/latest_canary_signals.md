# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T16:02:24.006740+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0075` n `12`; crypto_alt avg `0.0184` n `230`; crypto_major avg `-0.1843` n `8`; equity avg `-0.1885` n `121`; fx avg `0.018` n `6`; index avg `-0.0329` n `25`; metal avg `0.0114` n `20`; unknown avg `0.0237` n `793`
- 1h: commodity avg `0.0925` n `12`; crypto_alt avg `-0.2704` n `230`; crypto_major avg `-0.4613` n `8`; equity avg `0.2652` n `121`; fx avg `0.0306` n `6`; index avg `0.0608` n `25`; metal avg `0.0899` n `20`; unknown avg `0.0125` n `793`
- 4h: commodity avg `0.0346` n `12`; crypto_alt avg `1.3653` n `230`; crypto_major avg `1.1219` n `8`; equity avg `-0.3586` n `121`; fx avg `-0.0047` n `6`; index avg `-0.0247` n `25`; metal avg `-0.0523` n `20`; unknown avg `0.1164` n `793`
- 24h: commodity avg `0.2063` n `12`; crypto_alt avg `7.4989` n `230`; crypto_major avg `4.8595` n `8`; equity avg `1.4243` n `121`; fx avg `-0.0771` n `6`; index avg `0.1428` n `25`; metal avg `0.555` n `20`; unknown avg `2.3353` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.24`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.2029`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1951`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
