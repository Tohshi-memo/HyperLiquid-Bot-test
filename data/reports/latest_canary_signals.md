# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T11:52:29.372878+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0253` n `12`; crypto_alt avg `0.0832` n `230`; crypto_major avg `0.0562` n `8`; equity avg `-0.0088` n `92`; fx avg `0.0059` n `6`; index avg `0.0091` n `25`; metal avg `0.0096` n `20`; unknown avg `-0.0087` n `765`
- 1h: commodity avg `-0.0054` n `12`; crypto_alt avg `0.1468` n `230`; crypto_major avg `0.3793` n `8`; equity avg `0.0803` n `92`; fx avg `0.0004` n `6`; index avg `0.0054` n `25`; metal avg `0.0098` n `20`; unknown avg `-0.1001` n `763`
- 4h: commodity avg `0.0015` n `12`; crypto_alt avg `0.2186` n `230`; crypto_major avg `0.5084` n `8`; equity avg `0.1115` n `92`; fx avg `0.0029` n `6`; index avg `0.0136` n `25`; metal avg `0.0043` n `20`; unknown avg `-0.0134` n `763`
- 24h: commodity avg `0.4739` n `12`; crypto_alt avg `-0.7959` n `230`; crypto_major avg `-0.458` n `8`; equity avg `-0.14` n `92`; fx avg `0.0083` n `6`; index avg `-0.1176` n `25`; metal avg `-0.0909` n `20`; unknown avg `0.1203` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
