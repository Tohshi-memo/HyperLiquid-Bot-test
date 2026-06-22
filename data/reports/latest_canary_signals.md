# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T10:07:33.113003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.1733` n `228`; crypto_major avg `0.2228` n `8`; equity avg `0.0978` n `79`; fx avg `-0.0048` n `6`; index avg `0.0411` n `23`; metal avg `0.0384` n `18`; unknown avg `0.0285` n `701`
- 1h: commodity avg `0.0155` n `12`; crypto_alt avg `0.0769` n `228`; crypto_major avg `0.1467` n `8`; equity avg `0.0747` n `79`; fx avg `0.0106` n `6`; index avg `0.0327` n `23`; metal avg `0.032` n `18`; unknown avg `0.0405` n `701`
- 4h: commodity avg `0.1211` n `12`; crypto_alt avg `0.4745` n `228`; crypto_major avg `0.604` n `8`; equity avg `0.5041` n `79`; fx avg `0.0682` n `6`; index avg `0.0997` n `23`; metal avg `0.0868` n `18`; unknown avg `-0.0916` n `693`
- 24h: commodity avg `-0.2126` n `12`; crypto_alt avg `-0.2538` n `228`; crypto_major avg `0.0572` n `8`; equity avg `-0.079` n `79`; fx avg `0.0374` n `6`; index avg `0.0657` n `23`; metal avg `0.5241` n `18`; unknown avg `0.0887` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
