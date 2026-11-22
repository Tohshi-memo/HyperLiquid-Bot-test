# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T08:22:25.408631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `13`; crypto_alt avg `0.802` n `239`; crypto_major avg `0.9238` n `8`; equity avg `0.2637` n `166`; fx avg `-0.0002` n `6`; index avg `0.0311` n `27`; metal avg `0.0412` n `20`; unknown avg `160.9048` n `1245`
- 1h: commodity avg `0.0626` n `13`; crypto_alt avg `1.174` n `239`; crypto_major avg `1.0468` n `8`; equity avg `0.3074` n `166`; fx avg `-0.0033` n `6`; index avg `0.038` n `27`; metal avg `0.0361` n `20`; unknown avg `160.8715` n `1245`
- 4h: commodity avg `0.0479` n `13`; crypto_alt avg `0.9787` n `239`; crypto_major avg `0.827` n `8`; equity avg `0.2369` n `166`; fx avg `-0.0212` n `6`; index avg `0.0347` n `27`; metal avg `0.0516` n `20`; unknown avg `0.4621` n `1209`
- 24h: commodity avg `0.0568` n `13`; crypto_alt avg `3.108` n `239`; crypto_major avg `3.9246` n `8`; equity avg `1.0989` n `166`; fx avg `0.0416` n `6`; index avg `0.1597` n `27`; metal avg `0.138` n `20`; unknown avg `608.4312` n `1072`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
