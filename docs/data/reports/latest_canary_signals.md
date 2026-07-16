# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T22:22:26.969327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0072` n `12`; crypto_alt avg `-0.2362` n `230`; crypto_major avg `-0.2096` n `8`; equity avg `-0.2355` n `94`; fx avg `-0.0051` n `6`; index avg `-0.0506` n `25`; metal avg `-0.0371` n `20`; unknown avg `-0.1218` n `768`
- 1h: commodity avg `0.002` n `12`; crypto_alt avg `-0.1474` n `230`; crypto_major avg `-0.1301` n `8`; equity avg `-0.1483` n `94`; fx avg `-0.0103` n `6`; index avg `-0.0298` n `25`; metal avg `-0.0269` n `20`; unknown avg `-0.1005` n `768`
- 4h: commodity avg `0.2449` n `12`; crypto_alt avg `-0.2411` n `230`; crypto_major avg `-0.2357` n `8`; equity avg `-0.621` n `94`; fx avg `-0.0125` n `6`; index avg `-0.0793` n `25`; metal avg `-0.1456` n `20`; unknown avg `-0.3731` n `768`
- 24h: commodity avg `-0.1781` n `12`; crypto_alt avg `-1.0484` n `230`; crypto_major avg `-2.1008` n `8`; equity avg `-3.951` n `94`; fx avg `-0.1774` n `6`; index avg `-0.5581` n `25`; metal avg `-0.8798` n `20`; unknown avg `-0.4358` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
