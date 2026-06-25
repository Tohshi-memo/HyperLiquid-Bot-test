# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T01:22:31.984529+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0179` n `12`; crypto_alt avg `0.0529` n `228`; crypto_major avg `0.1787` n `8`; equity avg `0.1532` n `86`; fx avg `0.0168` n `6`; index avg `0.0338` n `23`; metal avg `-0.0002` n `20`; unknown avg `-0.0419` n `764`
- 1h: commodity avg `-0.0748` n `12`; crypto_alt avg `-0.2813` n `228`; crypto_major avg `-0.1571` n `8`; equity avg `-0.4621` n `86`; fx avg `0.0193` n `6`; index avg `-0.0342` n `23`; metal avg `-0.0948` n `20`; unknown avg `-0.3204` n `764`
- 4h: commodity avg `-0.0305` n `12`; crypto_alt avg `0.436` n `228`; crypto_major avg `0.5218` n `8`; equity avg `0.0619` n `86`; fx avg `0.0611` n `6`; index avg `-0.0444` n `23`; metal avg `-0.0859` n `20`; unknown avg `-0.8398` n `748`
- 24h: commodity avg `-0.5056` n `12`; crypto_alt avg `-2.4234` n `228`; crypto_major avg `-2.1267` n `8`; equity avg `4.0025` n `86`; fx avg `0.0938` n `6`; index avg `0.4229` n `23`; metal avg `-1.5061` n `20`; unknown avg `-1.2102` n `716`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
