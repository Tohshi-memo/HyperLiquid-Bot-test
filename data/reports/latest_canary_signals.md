# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T06:07:30.602344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1242` n `12`; crypto_alt avg `-0.1359` n `228`; crypto_major avg `-0.0942` n `8`; equity avg `0.0628` n `86`; fx avg `0.0138` n `6`; index avg `0.002` n `23`; metal avg `0.2255` n `20`; unknown avg `-0.0116` n `748`
- 1h: commodity avg `0.1111` n `12`; crypto_alt avg `0.3314` n `228`; crypto_major avg `0.2894` n `8`; equity avg `0.3781` n `86`; fx avg `0.0016` n `6`; index avg `0.0532` n `23`; metal avg `0.4489` n `20`; unknown avg `0.2399` n `748`
- 4h: commodity avg `0.0469` n `12`; crypto_alt avg `-0.197` n `228`; crypto_major avg `-0.0971` n `8`; equity avg `0.0187` n `86`; fx avg `0.0543` n `6`; index avg `-0.0272` n `23`; metal avg `0.2153` n `20`; unknown avg `-0.1226` n `740`
- 24h: commodity avg `-0.2303` n `12`; crypto_alt avg `-1.5168` n `228`; crypto_major avg `-1.5826` n `8`; equity avg `4.7826` n `86`; fx avg `-0.0946` n `6`; index avg `-0.0407` n `23`; metal avg `-0.1468` n `20`; unknown avg `-0.1416` n `580`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
