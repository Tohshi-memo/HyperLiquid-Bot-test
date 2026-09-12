# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T16:07:30.921652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `12`; crypto_alt avg `0.0688` n `233`; crypto_major avg `-0.0182` n `8`; equity avg `-0.0032` n `136`; fx avg `-0.0012` n `6`; index avg `-0.0005` n `26`; metal avg `0.0046` n `20`; unknown avg `-1.0377` n `836`
- 1h: commodity avg `-0.0012` n `12`; crypto_alt avg `0.1068` n `233`; crypto_major avg `-0.1766` n `8`; equity avg `0.0013` n `136`; fx avg `-0.0043` n `6`; index avg `0.0068` n `26`; metal avg `0.013` n `20`; unknown avg `-0.061` n `836`
- 4h: commodity avg `-0.0305` n `12`; crypto_alt avg `0.2711` n `233`; crypto_major avg `-0.1179` n `8`; equity avg `-0.0279` n `136`; fx avg `-0.0015` n `6`; index avg `0.0128` n `26`; metal avg `0.0142` n `20`; unknown avg `2.2403` n `824`
- 24h: commodity avg `-0.2512` n `12`; crypto_alt avg `0.2272` n `233`; crypto_major avg `-0.7857` n `8`; equity avg `-0.4052` n `136`; fx avg `-0.0263` n `6`; index avg `-0.0119` n `26`; metal avg `-0.0591` n `20`; unknown avg `12.3191` n `694`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0489`, n `668`, weak_sample_signal
