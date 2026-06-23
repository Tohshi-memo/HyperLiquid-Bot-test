# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T14:37:30.239644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0465` n `12`; crypto_alt avg `0.1736` n `228`; crypto_major avg `0.1964` n `8`; equity avg `0.0908` n `86`; fx avg `-0.0179` n `6`; index avg `-0.0851` n `23`; metal avg `-0.1096` n `20`; unknown avg `0.0905` n `764`
- 1h: commodity avg `-0.0114` n `12`; crypto_alt avg `0.4521` n `228`; crypto_major avg `0.4638` n `8`; equity avg `1.4563` n `86`; fx avg `-0.0224` n `6`; index avg `0.1854` n `23`; metal avg `-0.0664` n `20`; unknown avg `0.2303` n `764`
- 4h: commodity avg `-0.3209` n `12`; crypto_alt avg `1.1156` n `228`; crypto_major avg `0.7867` n `8`; equity avg `1.7263` n `86`; fx avg `-0.0698` n `6`; index avg `0.1126` n `23`; metal avg `-0.1448` n `20`; unknown avg `0.4429` n `764`
- 24h: commodity avg `-0.5426` n `12`; crypto_alt avg `-3.3629` n `228`; crypto_major avg `-3.9193` n `8`; equity avg `-2.7798` n `85`; fx avg `-0.1788` n `6`; index avg `-0.8686` n `23`; metal avg `-1.1835` n `20`; unknown avg `-0.0944` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
