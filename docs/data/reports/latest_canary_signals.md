# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T18:07:35.880976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0333` n `12`; crypto_alt avg `-0.1003` n `228`; crypto_major avg `-0.2402` n `8`; equity avg `-0.2625` n `86`; fx avg `-0.0003` n `6`; index avg `-0.0559` n `23`; metal avg `-0.068` n `20`; unknown avg `-0.1144` n `764`
- 1h: commodity avg `0.0517` n `12`; crypto_alt avg `-0.1269` n `228`; crypto_major avg `-0.0969` n `8`; equity avg `-0.2946` n `86`; fx avg `-0.0039` n `6`; index avg `-0.0589` n `23`; metal avg `-0.1121` n `20`; unknown avg `-0.3263` n `764`
- 4h: commodity avg `0.0544` n `12`; crypto_alt avg `-0.9226` n `228`; crypto_major avg `-0.704` n `8`; equity avg `-0.9785` n `86`; fx avg `-0.0558` n `6`; index avg `-0.1626` n `23`; metal avg `-0.1585` n `20`; unknown avg `-0.8361` n `764`
- 24h: commodity avg `-0.3991` n `12`; crypto_alt avg `-4.1092` n `228`; crypto_major avg `-4.6329` n `8`; equity avg `-3.5144` n `86`; fx avg `-0.1782` n `6`; index avg `-0.9829` n `23`; metal avg `-1.0529` n `20`; unknown avg `-0.5036` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
