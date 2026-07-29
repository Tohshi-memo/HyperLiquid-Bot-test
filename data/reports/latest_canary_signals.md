# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T14:07:25.606789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.67` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0823` n `12`; crypto_alt avg `0.0319` n `230`; crypto_major avg `0.0631` n `8`; equity avg `0.339` n `102`; fx avg `0.0051` n `6`; index avg `0.0422` n `25`; metal avg `-0.0284` n `20`; unknown avg `0.0281` n `777`
- 1h: commodity avg `0.0328` n `12`; crypto_alt avg `0.1017` n `230`; crypto_major avg `0.0627` n `8`; equity avg `-0.7953` n `102`; fx avg `0.0176` n `6`; index avg `-0.0737` n `25`; metal avg `-0.1034` n `20`; unknown avg `0.3346` n `777`
- 4h: commodity avg `0.3909` n `12`; crypto_alt avg `-0.4959` n `230`; crypto_major avg `-0.4287` n `8`; equity avg `-1.4282` n `102`; fx avg `0.0247` n `6`; index avg `-0.1517` n `25`; metal avg `-0.2044` n `20`; unknown avg `0.4394` n `777`
- 24h: commodity avg `0.5188` n `12`; crypto_alt avg `-1.2016` n `230`; crypto_major avg `1.2287` n `8`; equity avg `0.6583` n `102`; fx avg `-0.0721` n `6`; index avg `-0.0614` n `25`; metal avg `-0.2044` n `20`; unknown avg `0.1805` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
