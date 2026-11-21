# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T01:22:25.785370+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `13`; crypto_alt avg `0.0526` n `239`; crypto_major avg `0.1069` n `8`; equity avg `-0.0984` n `166`; fx avg `0.0014` n `6`; index avg `-0.0148` n `27`; metal avg `0.0012` n `20`; unknown avg `0.6827` n `1260`
- 1h: commodity avg `-0.0135` n `13`; crypto_alt avg `-0.0214` n `239`; crypto_major avg `0.1277` n `8`; equity avg `0.19` n `166`; fx avg `0.0124` n `6`; index avg `0.0097` n `27`; metal avg `0.0337` n `20`; unknown avg `3.0673` n `1258`
- 4h: commodity avg `-0.0441` n `13`; crypto_alt avg `0.97` n `239`; crypto_major avg `0.9741` n `8`; equity avg `0.7055` n `166`; fx avg `-0.024` n `6`; index avg `0.0914` n `27`; metal avg `0.1594` n `20`; unknown avg `166.0618` n `1228`
- 24h: commodity avg `0.3216` n `13`; crypto_alt avg `-5.0371` n `239`; crypto_major avg `-5.7671` n `8`; equity avg `-5.2448` n `166`; fx avg `-0.0144` n `6`; index avg `-0.5796` n `27`; metal avg `-0.3035` n `20`; unknown avg `16.2032` n `1121`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
