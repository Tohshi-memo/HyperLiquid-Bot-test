# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T17:07:29.346850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `12`; crypto_alt avg `-0.0486` n `230`; crypto_major avg `-0.0586` n `8`; equity avg `0.0877` n `92`; fx avg `0.0137` n `6`; index avg `0.0377` n `25`; metal avg `0.0277` n `20`; unknown avg `-0.0003` n `766`
- 1h: commodity avg `0.1698` n `12`; crypto_alt avg `-0.4461` n `230`; crypto_major avg `-0.3902` n `8`; equity avg `-0.385` n `92`; fx avg `0.0203` n `6`; index avg `-0.0338` n `25`; metal avg `-0.1516` n `20`; unknown avg `0.0152` n `766`
- 4h: commodity avg `0.3988` n `12`; crypto_alt avg `-0.3624` n `230`; crypto_major avg `-0.4022` n `8`; equity avg `-0.7577` n `92`; fx avg `-0.0148` n `6`; index avg `-0.1132` n `25`; metal avg `-0.3822` n `20`; unknown avg `-0.0495` n `766`
- 24h: commodity avg `0.2296` n `12`; crypto_alt avg `-1.8726` n `230`; crypto_major avg `-2.8654` n `8`; equity avg `-2.8548` n `92`; fx avg `-0.07` n `6`; index avg `-0.5663` n `25`; metal avg `-0.5465` n `20`; unknown avg `-0.1194` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1997`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
