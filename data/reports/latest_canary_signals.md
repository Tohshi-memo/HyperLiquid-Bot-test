# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T00:52:28.041451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0121` n `12`; crypto_alt avg `0.2355` n `228`; crypto_major avg `0.1514` n `8`; equity avg `0.2643` n `86`; fx avg `-0.0017` n `6`; index avg `0.0654` n `23`; metal avg `0.1034` n `20`; unknown avg `-0.0482` n `716`
- 1h: commodity avg `-0.028` n `12`; crypto_alt avg `0.3382` n `228`; crypto_major avg `0.093` n `8`; equity avg `-0.3781` n `86`; fx avg `0.0025` n `6`; index avg `-0.086` n `23`; metal avg `0.0273` n `20`; unknown avg `0.0104` n `716`
- 4h: commodity avg `-0.0244` n `12`; crypto_alt avg `-0.5558` n `228`; crypto_major avg `-0.4038` n `8`; equity avg `-0.6843` n `86`; fx avg `0.015` n `6`; index avg `-0.1649` n `23`; metal avg `-0.0355` n `20`; unknown avg `-0.6126` n `716`
- 24h: commodity avg `-0.9001` n `12`; crypto_alt avg `-0.825` n `228`; crypto_major avg `-0.319` n `8`; equity avg `-0.7278` n `85`; fx avg `0.0917` n `6`; index avg `-0.0602` n `23`; metal avg `-0.1207` n `18`; unknown avg `0.0396` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
