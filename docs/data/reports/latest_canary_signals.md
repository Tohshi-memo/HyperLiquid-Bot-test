# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T10:07:30.678687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0144` n `12`; crypto_alt avg `0.0459` n `228`; crypto_major avg `0.0966` n `8`; equity avg `0.0209` n `78`; fx avg `0.0039` n `6`; index avg `-0.0016` n `23`; metal avg `-0.0057` n `18`; unknown avg `0.1834` n `687`
- 1h: commodity avg `0.023` n `12`; crypto_alt avg `0.3032` n `228`; crypto_major avg `0.3114` n `8`; equity avg `0.0146` n `78`; fx avg `0.3002` n `6`; index avg `0.0268` n `23`; metal avg `-0.0` n `18`; unknown avg `0.0558` n `687`
- 4h: commodity avg `0.0422` n `12`; crypto_alt avg `0.365` n `228`; crypto_major avg `0.1906` n `8`; equity avg `-0.091` n `78`; fx avg `0.0237` n `6`; index avg `-0.0075` n `23`; metal avg `0.0184` n `18`; unknown avg `-0.1374` n `671`
- 24h: commodity avg `0.5252` n `12`; crypto_alt avg `-2.742` n `228`; crypto_major avg `-3.1763` n `8`; equity avg `1.2495` n `78`; fx avg `-0.0886` n `6`; index avg `0.306` n `23`; metal avg `-4.109` n `18`; unknown avg `0.1044` n `530`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
