# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T14:52:36.763841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `12`; crypto_alt avg `0.091` n `228`; crypto_major avg `0.0501` n `8`; equity avg `-0.251` n `74`; fx avg `-0.0015` n `6`; index avg `-0.0485` n `23`; metal avg `-0.0717` n `18`; unknown avg `0.0637` n `556`
- 1h: commodity avg `0.2466` n `12`; crypto_alt avg `0.071` n `228`; crypto_major avg `-0.1712` n `8`; equity avg `-0.4818` n `74`; fx avg `-0.0512` n `6`; index avg `-0.1416` n `23`; metal avg `-0.1837` n `18`; unknown avg `0.0862` n `556`
- 4h: commodity avg `0.3394` n `12`; crypto_alt avg `0.301` n `228`; crypto_major avg `0.1809` n `8`; equity avg `-0.29` n `74`; fx avg `-0.0511` n `6`; index avg `-0.0772` n `23`; metal avg `0.1449` n `18`; unknown avg `0.6558` n `556`
- 24h: commodity avg `-0.3732` n `12`; crypto_alt avg `0.9751` n `228`; crypto_major avg `0.5751` n `8`; equity avg `-0.9959` n `74`; fx avg `-0.0363` n `6`; index avg `-0.4935` n `23`; metal avg `-0.7145` n `18`; unknown avg `2.5954` n `528`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
