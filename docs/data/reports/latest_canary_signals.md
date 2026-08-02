# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T08:07:25.384172+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0163` n `12`; crypto_alt avg `-0.0216` n `230`; crypto_major avg `-0.0905` n `8`; equity avg `0.0594` n `102`; fx avg `0.0137` n `6`; index avg `0.0186` n `25`; metal avg `-0.0064` n `20`; unknown avg `-0.0551` n `782`
- 1h: commodity avg `-0.0522` n `12`; crypto_alt avg `0.0678` n `230`; crypto_major avg `-0.0773` n `8`; equity avg `0.1623` n `102`; fx avg `-0.0114` n `6`; index avg `0.0295` n `25`; metal avg `0.0048` n `20`; unknown avg `-0.0686` n `782`
- 4h: commodity avg `0.0051` n `12`; crypto_alt avg `0.2757` n `230`; crypto_major avg `-0.1079` n `8`; equity avg `0.1346` n `102`; fx avg `-0.04` n `6`; index avg `0.0368` n `25`; metal avg `0.036` n `20`; unknown avg `0.324` n `766`
- 24h: commodity avg `-1.1688` n `12`; crypto_alt avg `0.5417` n `230`; crypto_major avg `0.4176` n `8`; equity avg `0.8606` n `102`; fx avg `-0.1449` n `6`; index avg `0.2464` n `25`; metal avg `0.2418` n `20`; unknown avg `0.2893` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
