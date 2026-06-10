# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T09:37:29.645622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2384` n `12`; crypto_alt avg `0.4305` n `228`; crypto_major avg `0.5326` n `8`; equity avg `0.3883` n `74`; fx avg `0.0036` n `6`; index avg `0.1774` n `23`; metal avg `0.2478` n `18`; unknown avg `0.045` n `547`
- 1h: commodity avg `-0.145` n `12`; crypto_alt avg `-0.2221` n `228`; crypto_major avg `-0.0332` n `8`; equity avg `-0.2758` n `74`; fx avg `0.001` n `6`; index avg `-0.1162` n `23`; metal avg `0.0876` n `18`; unknown avg `-0.0844` n `547`
- 4h: commodity avg `0.3769` n `12`; crypto_alt avg `0.1113` n `228`; crypto_major avg `-0.0431` n `8`; equity avg `-0.2212` n `74`; fx avg `0.0127` n `6`; index avg `-0.1276` n `23`; metal avg `0.1004` n `18`; unknown avg `-0.324` n `537`
- 24h: commodity avg `-0.2665` n `12`; crypto_alt avg `-1.2364` n `228`; crypto_major avg `-3.4766` n `8`; equity avg `-4.2794` n `74`; fx avg `0.0544` n `6`; index avg `-2.2625` n `23`; metal avg `-3.2176` n `18`; unknown avg `0.6074` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
