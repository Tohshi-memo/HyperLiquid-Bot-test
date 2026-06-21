# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T19:59:02.324231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0847` n `12`; crypto_alt avg `0.0291` n `228`; crypto_major avg `0.0546` n `8`; equity avg `-0.0074` n `78`; fx avg `-0.02` n `6`; index avg `0.0067` n `23`; metal avg `-0.0192` n `18`; unknown avg `-0.0197` n `702`
- 1h: commodity avg `-0.0413` n `12`; crypto_alt avg `0.077` n `228`; crypto_major avg `0.1434` n `8`; equity avg `-0.0145` n `78`; fx avg `-0.0245` n `6`; index avg `0.0205` n `23`; metal avg `-0.0119` n `18`; unknown avg `0.1783` n `694`
- 4h: commodity avg `0.198` n `12`; crypto_alt avg `-0.1017` n `228`; crypto_major avg `0.1471` n `8`; equity avg `-0.0783` n `78`; fx avg `-0.1133` n `6`; index avg `0.0072` n `23`; metal avg `-0.1017` n `18`; unknown avg `-0.0611` n `694`
- 24h: commodity avg `0.2827` n `12`; crypto_alt avg `1.6173` n `228`; crypto_major avg `0.5169` n `8`; equity avg `0.3292` n `78`; fx avg `0.0895` n `6`; index avg `0.0181` n `23`; metal avg `-0.0802` n `18`; unknown avg `0.3426` n `645`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
