# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T20:12:47.960789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0128` n `12`; crypto_alt avg `-0.0026` n `230`; crypto_major avg `-0.1245` n `8`; equity avg `-0.2917` n `102`; fx avg `-0.0371` n `6`; index avg `-0.0704` n `25`; metal avg `-0.06` n `20`; unknown avg `3.4798` n `780`
- 1h: commodity avg `0.0546` n `12`; crypto_alt avg `-0.1869` n `230`; crypto_major avg `-0.3359` n `8`; equity avg `-0.4943` n `102`; fx avg `-0.0284` n `6`; index avg `-0.0468` n `25`; metal avg `-0.0593` n `20`; unknown avg `-0.1701` n `780`
- 4h: commodity avg `0.171` n `12`; crypto_alt avg `0.0458` n `230`; crypto_major avg `-0.3054` n `8`; equity avg `0.3361` n `102`; fx avg `0.0528` n `6`; index avg `0.0939` n `25`; metal avg `0.0898` n `20`; unknown avg `7.1033` n `780`
- 24h: commodity avg `0.2573` n `12`; crypto_alt avg `-0.7816` n `230`; crypto_major avg `-2.3951` n `8`; equity avg `-0.7005` n `102`; fx avg `0.1901` n `6`; index avg `0.089` n `25`; metal avg `-0.4468` n `20`; unknown avg `0.2102` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
