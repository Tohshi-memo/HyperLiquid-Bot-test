# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T05:52:31.404626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0209` n `12`; crypto_alt avg `-0.1218` n `228`; crypto_major avg `0.0322` n `8`; equity avg `-0.0195` n `86`; fx avg `0.0151` n `6`; index avg `-0.0053` n `23`; metal avg `-0.0077` n `20`; unknown avg `1.8825` n `765`
- 1h: commodity avg `-0.0398` n `12`; crypto_alt avg `0.837` n `228`; crypto_major avg `0.794` n `8`; equity avg `0.1766` n `86`; fx avg `-0.0351` n `6`; index avg `0.0503` n `23`; metal avg `-0.1116` n `20`; unknown avg `25.1619` n `765`
- 4h: commodity avg `0.012` n `12`; crypto_alt avg `1.0119` n `228`; crypto_major avg `1.0078` n `8`; equity avg `0.2481` n `86`; fx avg `-0.0512` n `6`; index avg `0.1039` n `23`; metal avg `0.0113` n `20`; unknown avg `0.9474` n `748`
- 24h: commodity avg `-0.4952` n `12`; crypto_alt avg `-1.2399` n `228`; crypto_major avg `-1.0309` n `8`; equity avg `0.0024` n `86`; fx avg `0.0094` n `6`; index avg `0.5762` n `23`; metal avg `-1.6311` n `20`; unknown avg `-0.5631` n `708`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
