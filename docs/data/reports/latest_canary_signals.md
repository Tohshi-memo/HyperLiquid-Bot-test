# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T13:22:32.160557+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0291` n `12`; crypto_alt avg `0.1095` n `228`; crypto_major avg `0.1172` n `8`; equity avg `0.0593` n `74`; fx avg `0.0227` n `6`; index avg `-0.2115` n `23`; metal avg `-0.339` n `18`; unknown avg `0.0298` n `547`
- 1h: commodity avg `0.0272` n `12`; crypto_alt avg `1.3255` n `228`; crypto_major avg `1.0363` n `8`; equity avg `0.9721` n `74`; fx avg `0.0163` n `6`; index avg `0.3294` n `23`; metal avg `0.6264` n `18`; unknown avg `0.3015` n `547`
- 4h: commodity avg `1.3648` n `12`; crypto_alt avg `1.1055` n `228`; crypto_major avg `1.1767` n `8`; equity avg `0.8592` n `74`; fx avg `-0.0155` n `6`; index avg `0.1993` n `23`; metal avg `0.2167` n `18`; unknown avg `0.2844` n `547`
- 24h: commodity avg `0.8208` n `12`; crypto_alt avg `-1.0867` n `228`; crypto_major avg `-2.495` n `8`; equity avg `-3.8247` n `74`; fx avg `-0.0856` n `6`; index avg `-2.2193` n `23`; metal avg `-3.5611` n `18`; unknown avg `1.2147` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
