# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T11:22:26.630552+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1205` n `12`; crypto_alt avg `-0.0556` n `230`; crypto_major avg `-0.0436` n `8`; equity avg `-0.2349` n `102`; fx avg `0.0023` n `6`; index avg `-0.0504` n `25`; metal avg `0.0105` n `20`; unknown avg `-0.0334` n `780`
- 1h: commodity avg `0.1589` n `12`; crypto_alt avg `-0.0105` n `230`; crypto_major avg `0.1016` n `8`; equity avg `-0.0034` n `102`; fx avg `0.0041` n `6`; index avg `-0.0525` n `25`; metal avg `0.0085` n `20`; unknown avg `2.3171` n `780`
- 4h: commodity avg `0.4601` n `12`; crypto_alt avg `0.0103` n `230`; crypto_major avg `-0.1235` n `8`; equity avg `0.5679` n `102`; fx avg `0.0486` n `6`; index avg `0.0026` n `25`; metal avg `-0.0992` n `20`; unknown avg `0.2358` n `779`
- 24h: commodity avg `0.3849` n `12`; crypto_alt avg `-0.2072` n `230`; crypto_major avg `-0.1038` n `8`; equity avg `7.3438` n `102`; fx avg `-0.058` n `6`; index avg `1.0373` n `25`; metal avg `0.0494` n `20`; unknown avg `0.2613` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
