# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T22:45:14.377669+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `12`; crypto_alt avg `-0.0471` n `228`; crypto_major avg `0.0627` n `8`; equity avg `-0.0673` n `86`; fx avg `-0.0052` n `6`; index avg `-0.0032` n `23`; metal avg `0.0051` n `20`; unknown avg `0.0007` n `764`
- 1h: commodity avg `-0.0166` n `12`; crypto_alt avg `-0.1361` n `228`; crypto_major avg `0.0245` n `8`; equity avg `-0.2684` n `86`; fx avg `-0.03` n `6`; index avg `-0.0377` n `23`; metal avg `-0.1345` n `20`; unknown avg `-0.6008` n `764`
- 4h: commodity avg `-0.0769` n `12`; crypto_alt avg `0.4948` n `228`; crypto_major avg `0.4441` n `8`; equity avg `0.1334` n `86`; fx avg `-0.0243` n `6`; index avg `0.0804` n `23`; metal avg `-0.0227` n `20`; unknown avg `1.2052` n `756`
- 24h: commodity avg `-0.4749` n `12`; crypto_alt avg `-1.7468` n `228`; crypto_major avg `-2.8836` n `8`; equity avg `-3.2723` n `86`; fx avg `-0.1863` n `6`; index avg `-0.8985` n `23`; metal avg `-1.2376` n `20`; unknown avg `1.7228` n `596`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
