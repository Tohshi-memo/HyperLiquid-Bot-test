# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T06:37:28.357766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0239` n `12`; crypto_alt avg `0.0328` n `228`; crypto_major avg `0.0857` n `8`; equity avg `0.0311` n `86`; fx avg `0.0209` n `6`; index avg `0.0088` n `23`; metal avg `-0.0168` n `20`; unknown avg `-0.1492` n `764`
- 1h: commodity avg `-0.0218` n `12`; crypto_alt avg `-0.2391` n `228`; crypto_major avg `-0.153` n `8`; equity avg `-0.022` n `86`; fx avg `0.0321` n `6`; index avg `-0.0089` n `23`; metal avg `0.1575` n `20`; unknown avg `0.0325` n `748`
- 4h: commodity avg `0.0119` n `12`; crypto_alt avg `-0.118` n `228`; crypto_major avg `0.2395` n `8`; equity avg `0.2181` n `86`; fx avg `0.0827` n `6`; index avg `0.0581` n `23`; metal avg `0.2757` n `20`; unknown avg `-0.0566` n `740`
- 24h: commodity avg `-0.3205` n `12`; crypto_alt avg `-0.4225` n `228`; crypto_major avg `-0.7549` n `8`; equity avg `4.9232` n `86`; fx avg `-0.1022` n `6`; index avg `0.1509` n `23`; metal avg `-0.1225` n `20`; unknown avg `-0.0022` n `580`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
