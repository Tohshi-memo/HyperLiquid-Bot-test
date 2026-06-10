# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T18:37:30.189765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1626` n `12`; crypto_alt avg `-0.1681` n `228`; crypto_major avg `-0.2416` n `8`; equity avg `-0.2469` n `74`; fx avg `-0.0064` n `6`; index avg `-0.1681` n `23`; metal avg `-0.096` n `18`; unknown avg `0.3793` n `550`
- 1h: commodity avg `-0.6054` n `12`; crypto_alt avg `-0.3464` n `228`; crypto_major avg `-0.3438` n `8`; equity avg `-0.0647` n `74`; fx avg `0.0087` n `6`; index avg `-0.1464` n `23`; metal avg `0.1163` n `18`; unknown avg `-0.2569` n `550`
- 4h: commodity avg `-0.1552` n `12`; crypto_alt avg `-1.2384` n `228`; crypto_major avg `-1.3116` n `8`; equity avg `-1.651` n `74`; fx avg `-0.0126` n `6`; index avg `-1.3145` n `23`; metal avg `-0.6979` n `18`; unknown avg `0.3219` n `548`
- 24h: commodity avg `0.9387` n `12`; crypto_alt avg `-1.475` n `228`; crypto_major avg `-2.2212` n `8`; equity avg `-1.0145` n `74`; fx avg `-0.0395` n `6`; index avg `-0.6645` n `23`; metal avg `-1.7688` n `18`; unknown avg `-0.1545` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
