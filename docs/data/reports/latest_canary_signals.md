# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T05:17:04.014243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `12`; crypto_alt avg `0.0374` n `230`; crypto_major avg `0.0232` n `8`; equity avg `-0.0818` n `114`; fx avg `-0.0106` n `6`; index avg `-0.0192` n `25`; metal avg `0.006` n `20`; unknown avg `-0.2009` n `793`
- 1h: commodity avg `0.01` n `12`; crypto_alt avg `0.2085` n `230`; crypto_major avg `0.1836` n `8`; equity avg `-0.0851` n `114`; fx avg `-0.0026` n `6`; index avg `-0.0277` n `25`; metal avg `0.0203` n `20`; unknown avg `-0.1331` n `793`
- 4h: commodity avg `0.074` n `12`; crypto_alt avg `-0.8283` n `230`; crypto_major avg `-0.2584` n `8`; equity avg `-1.6433` n `114`; fx avg `0.0125` n `6`; index avg `-0.2911` n `25`; metal avg `-0.2652` n `20`; unknown avg `-0.0194` n `793`
- 24h: commodity avg `0.7011` n `12`; crypto_alt avg `-1.3544` n `230`; crypto_major avg `0.0167` n `8`; equity avg `-1.2389` n `114`; fx avg `-0.0104` n `6`; index avg `-0.3269` n `25`; metal avg `-0.2113` n `20`; unknown avg `-0.0129` n `776`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1872`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
