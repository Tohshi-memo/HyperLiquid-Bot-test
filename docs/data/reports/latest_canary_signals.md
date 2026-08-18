# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T03:52:31.679807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0257` n `12`; crypto_alt avg `0.0281` n `230`; crypto_major avg `0.0924` n `8`; equity avg `0.2412` n `114`; fx avg `0.0061` n `6`; index avg `0.0259` n `25`; metal avg `-0.0102` n `20`; unknown avg `0.0285` n `793`
- 1h: commodity avg `0.0322` n `12`; crypto_alt avg `-0.2639` n `230`; crypto_major avg `0.0633` n `8`; equity avg `0.0805` n `114`; fx avg `0.0284` n `6`; index avg `-0.0328` n `25`; metal avg `-0.0319` n `20`; unknown avg `-0.1687` n `793`
- 4h: commodity avg `0.0447` n `12`; crypto_alt avg `-1.2221` n `230`; crypto_major avg `-0.6132` n `8`; equity avg `-1.4739` n `114`; fx avg `-0.0465` n `6`; index avg `-0.2571` n `25`; metal avg `-0.2448` n `20`; unknown avg `0.6716` n `793`
- 24h: commodity avg `0.6339` n `12`; crypto_alt avg `-1.4951` n `230`; crypto_major avg `-0.1006` n `8`; equity avg `-1.03` n `114`; fx avg `-0.0217` n `6`; index avg `-0.2794` n `25`; metal avg `-0.1868` n `20`; unknown avg `-0.0069` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2133`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1668`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
