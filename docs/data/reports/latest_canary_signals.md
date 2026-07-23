# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T21:39:29.775462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0159` n `12`; crypto_alt avg `0.0029` n `230`; crypto_major avg `-0.0479` n `8`; equity avg `-0.1077` n `100`; fx avg `-0.0073` n `6`; index avg `-0.0017` n `25`; metal avg `-0.0014` n `20`; unknown avg `-0.1715` n `772`
- 1h: commodity avg `0.0881` n `12`; crypto_alt avg `-0.262` n `230`; crypto_major avg `-0.2589` n `8`; equity avg `-0.3065` n `100`; fx avg `-0.0214` n `6`; index avg `-0.0319` n `25`; metal avg `0.0205` n `20`; unknown avg `-0.0364` n `772`
- 4h: commodity avg `-0.0762` n `12`; crypto_alt avg `-0.2615` n `230`; crypto_major avg `-0.1444` n `8`; equity avg `-0.1656` n `100`; fx avg `-0.0041` n `6`; index avg `0.0811` n `25`; metal avg `0.0309` n `20`; unknown avg `-0.0106` n `772`
- 24h: commodity avg `0.8359` n `12`; crypto_alt avg `-1.6375` n `230`; crypto_major avg `-2.1653` n `8`; equity avg `-1.4302` n `99`; fx avg `-0.0805` n `6`; index avg `-0.2599` n `25`; metal avg `-0.7581` n `20`; unknown avg `-0.2488` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
