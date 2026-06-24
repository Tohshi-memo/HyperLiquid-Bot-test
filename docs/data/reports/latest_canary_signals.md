# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T11:07:31.579416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0435` n `12`; crypto_alt avg `-0.1443` n `228`; crypto_major avg `-0.1947` n `8`; equity avg `-0.0739` n `86`; fx avg `-0.0026` n `6`; index avg `-0.0275` n `23`; metal avg `-0.1047` n `20`; unknown avg `-0.0011` n `764`
- 1h: commodity avg `-0.0348` n `12`; crypto_alt avg `-0.5303` n `228`; crypto_major avg `-0.4875` n `8`; equity avg `-0.083` n `86`; fx avg `-0.0388` n `6`; index avg `0.0144` n `23`; metal avg `-0.2169` n `20`; unknown avg `-0.0363` n `764`
- 4h: commodity avg `-0.0246` n `12`; crypto_alt avg `-0.5685` n `228`; crypto_major avg `-0.6015` n `8`; equity avg `-0.1085` n `86`; fx avg `-0.0618` n `6`; index avg `0.0205` n `23`; metal avg `-0.557` n `20`; unknown avg `-0.3272` n `764`
- 24h: commodity avg `-0.4947` n `12`; crypto_alt avg `-0.2941` n `228`; crypto_major avg `-0.4232` n `8`; equity avg `4.5786` n `86`; fx avg `-0.0301` n `6`; index avg `0.1343` n `23`; metal avg `-0.797` n `20`; unknown avg `-0.0717` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
