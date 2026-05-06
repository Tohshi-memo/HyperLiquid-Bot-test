# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T20:52:25.901215+00:00`
- Correlation status: `ready`
- Asset price records: `487`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.19` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0232` n `12`; crypto_alt avg `-0.1611` n `228`; crypto_major avg `-0.1652` n `8`; equity avg `-0.2556` n `65`; fx avg `0.0115` n `4`; index avg `-0.0779` n `23`; metal avg `-0.0897` n `18`; unknown avg `-0.0757` n `356`
- 1h: commodity avg `0.3216` n `12`; crypto_alt avg `-0.0747` n `228`; crypto_major avg `-0.2944` n `8`; equity avg `-0.1298` n `65`; fx avg `0.01` n `4`; index avg `-0.0671` n `23`; metal avg `-0.1073` n `18`; unknown avg `0.0409` n `356`
- 4h: commodity avg `-0.0223` n `12`; crypto_alt avg `-0.5211` n `228`; crypto_major avg `-0.5433` n `8`; equity avg `0.5847` n `65`; fx avg `-0.0599` n `4`; index avg `0.3471` n `23`; metal avg `0.1397` n `18`; unknown avg `-0.3368` n `356`
- 24h: commodity avg `-2.3432` n `7`; crypto_alt avg `1.503` n `223`; crypto_major avg `-0.1403` n `7`; equity avg `2.7024` n `47`; fx avg `-0.4762` n `4`; index avg `1.5493` n `6`; metal avg `3.3975` n `7`; unknown avg `3.6871` n `311`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1796`, n `479`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1675`, n `479`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1491`, n `479`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1392`, n `479`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1339`, n `483`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.12`, n `483`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.098`, n `479`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `483`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.074`, n `479`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0682`, n `483`, weak_sample_signal
