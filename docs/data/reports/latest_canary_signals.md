# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T10:07:35.042276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0468` n `12`; crypto_alt avg `0.0344` n `228`; crypto_major avg `-0.0868` n `8`; equity avg `0.0003` n `86`; fx avg `-0.0009` n `6`; index avg `-0.0107` n `23`; metal avg `-0.1229` n `20`; unknown avg `-0.0135` n `764`
- 1h: commodity avg `0.0631` n `12`; crypto_alt avg `-0.1442` n `228`; crypto_major avg `-0.156` n `8`; equity avg `-0.0482` n `86`; fx avg `-0.0048` n `6`; index avg `-0.0083` n `23`; metal avg `-0.1187` n `20`; unknown avg `-0.1749` n `764`
- 4h: commodity avg `-0.1525` n `12`; crypto_alt avg `-0.1978` n `228`; crypto_major avg `-0.3107` n `8`; equity avg `-0.1163` n `86`; fx avg `0.0247` n `6`; index avg `0.0244` n `23`; metal avg `-0.5114` n `20`; unknown avg `-0.411` n `756`
- 24h: commodity avg `-0.3878` n `12`; crypto_alt avg `0.0243` n `228`; crypto_major avg `-0.0625` n `8`; equity avg `4.5031` n `86`; fx avg `0.0098` n `6`; index avg `0.0528` n `23`; metal avg `-0.7491` n `20`; unknown avg `-0.0243` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
