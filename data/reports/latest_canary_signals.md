# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T04:07:30.673335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `0.0291` n `230`; crypto_major avg `-0.0292` n `8`; equity avg `-0.0381` n `114`; fx avg `-0.0044` n `6`; index avg `0.0072` n `25`; metal avg `-0.0119` n `20`; unknown avg `0.0991` n `793`
- 1h: commodity avg `0.0399` n `12`; crypto_alt avg `0.0709` n `230`; crypto_major avg `0.0319` n `8`; equity avg `0.1406` n `114`; fx avg `0.0377` n `6`; index avg `-0.0225` n `25`; metal avg `-0.0565` n `20`; unknown avg `-0.175` n `793`
- 4h: commodity avg `0.0611` n `12`; crypto_alt avg `-1.0429` n `230`; crypto_major avg `-0.546` n `8`; equity avg `-1.5431` n `114`; fx avg `-0.0264` n `6`; index avg `-0.2345` n `25`; metal avg `-0.2694` n `20`; unknown avg `0.2117` n `793`
- 24h: commodity avg `0.6885` n `12`; crypto_alt avg `-1.5297` n `230`; crypto_major avg `-0.1502` n `8`; equity avg `-1.0371` n `114`; fx avg `-0.0263` n `6`; index avg `-0.285` n `25`; metal avg `-0.2282` n `20`; unknown avg `-0.0542` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
