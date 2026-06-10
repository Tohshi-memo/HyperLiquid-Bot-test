# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T13:52:33.257065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.176` n `12`; crypto_alt avg `0.1694` n `228`; crypto_major avg `0.1566` n `8`; equity avg `0.6087` n `74`; fx avg `0.0032` n `6`; index avg `0.1552` n `23`; metal avg `0.4507` n `18`; unknown avg `1.2305` n `547`
- 1h: commodity avg `-0.1048` n `12`; crypto_alt avg `1.1392` n `228`; crypto_major avg `1.1377` n `8`; equity avg `1.3646` n `74`; fx avg `0.0494` n `6`; index avg `0.2919` n `23`; metal avg `1.0994` n `18`; unknown avg `1.1373` n `547`
- 4h: commodity avg `0.8342` n `12`; crypto_alt avg `1.8342` n `228`; crypto_major avg `1.9374` n `8`; equity avg `2.1223` n `74`; fx avg `0.0079` n `6`; index avg `0.6446` n `23`; metal avg `1.2863` n `18`; unknown avg `1.4487` n `547`
- 24h: commodity avg `1.1635` n `12`; crypto_alt avg `-0.3239` n `228`; crypto_major avg `-1.5662` n `8`; equity avg `-2.6205` n `74`; fx avg `-0.0247` n `6`; index avg `-1.7847` n `23`; metal avg `-2.459` n `18`; unknown avg `1.5112` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
