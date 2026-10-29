# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T10:37:36.771288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `13`; crypto_alt avg `0.4333` n `238`; crypto_major avg `0.6188` n `8`; equity avg `0.0917` n `155`; fx avg `0.0137` n `6`; index avg `-0.0232` n `27`; metal avg `-0.0138` n `20`; unknown avg `0.0459` n `1190`
- 1h: commodity avg `-0.1305` n `13`; crypto_alt avg `0.6278` n `238`; crypto_major avg `0.5334` n `8`; equity avg `0.1869` n `155`; fx avg `0.0492` n `6`; index avg `-0.0117` n `27`; metal avg `0.0499` n `20`; unknown avg `0.3196` n `1144`
- 4h: commodity avg `-0.0805` n `13`; crypto_alt avg `0.4431` n `238`; crypto_major avg `0.4032` n `8`; equity avg `0.0515` n `155`; fx avg `0.0595` n `6`; index avg `0.017` n `27`; metal avg `-0.0772` n `20`; unknown avg `-0.094` n `1120`
- 24h: commodity avg `-0.1812` n `13`; crypto_alt avg `-2.2098` n `238`; crypto_major avg `-1.6781` n `8`; equity avg `-1.5791` n `155`; fx avg `0.073` n `6`; index avg `-0.0425` n `27`; metal avg `-0.3617` n `20`; unknown avg `9.5897` n `982`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
