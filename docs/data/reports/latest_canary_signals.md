# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T01:37:29.342093+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.015` n `12`; crypto_alt avg `0.4517` n `228`; crypto_major avg `0.5546` n `8`; equity avg `0.2813` n `86`; fx avg `-0.0016` n `6`; index avg `0.0411` n `23`; metal avg `0.1724` n `20`; unknown avg `0.4666` n `764`
- 1h: commodity avg `0.0316` n `12`; crypto_alt avg `0.1773` n `228`; crypto_major avg `0.4194` n `8`; equity avg `-0.0086` n `86`; fx avg `-0.0086` n `6`; index avg `-0.063` n `23`; metal avg `0.0577` n `20`; unknown avg `-0.2967` n `764`
- 4h: commodity avg `-0.0312` n `12`; crypto_alt avg `0.332` n `228`; crypto_major avg `0.8949` n `8`; equity avg `0.545` n `86`; fx avg `0.026` n `6`; index avg `0.1211` n `23`; metal avg `-0.0931` n `20`; unknown avg `0.0629` n `756`
- 24h: commodity avg `-0.4506` n `12`; crypto_alt avg `-1.5822` n `228`; crypto_major avg `-2.0405` n `8`; equity avg `-1.628` n `86`; fx avg `-0.1548` n `6`; index avg `-0.5253` n `23`; metal avg `-0.9085` n `20`; unknown avg `0.23` n `588`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
