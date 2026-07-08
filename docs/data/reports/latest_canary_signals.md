# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T06:07:25.095376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0262` n `12`; crypto_alt avg `0.0633` n `229`; crypto_major avg `0.0188` n `8`; equity avg `0.0131` n `91`; fx avg `0.011` n `6`; index avg `0.011` n `25`; metal avg `-0.0356` n `20`; unknown avg `0.0206` n `745`
- 1h: commodity avg `0.0805` n `12`; crypto_alt avg `-0.1823` n `229`; crypto_major avg `-0.3064` n `8`; equity avg `-0.3381` n `91`; fx avg `-0.017` n `6`; index avg `-0.0927` n `25`; metal avg `-0.0958` n `20`; unknown avg `-0.0153` n `743`
- 4h: commodity avg `0.1459` n `12`; crypto_alt avg `-0.0204` n `229`; crypto_major avg `-0.3553` n `8`; equity avg `-0.1198` n `91`; fx avg `-0.0306` n `6`; index avg `-0.1335` n `25`; metal avg `0.1487` n `20`; unknown avg `-0.0456` n `743`
- 24h: commodity avg `0.903` n `12`; crypto_alt avg `-2.4566` n `229`; crypto_major avg `-2.0074` n `8`; equity avg `-1.5906` n `91`; fx avg `-0.2322` n `6`; index avg `-0.3351` n `25`; metal avg `0.0552` n `20`; unknown avg `-0.4112` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
