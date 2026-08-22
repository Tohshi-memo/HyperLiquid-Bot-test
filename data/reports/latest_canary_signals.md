# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T18:45:58.881599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.3081` n `230`; crypto_major avg `-0.2637` n `8`; equity avg `-0.0006` n `121`; fx avg `0.0052` n `6`; index avg `-0.0044` n `25`; metal avg `0.0002` n `20`; unknown avg `-0.0058` n `794`
- 1h: commodity avg `0.003` n `12`; crypto_alt avg `-0.4837` n `230`; crypto_major avg `-0.1187` n `8`; equity avg `-0.0067` n `121`; fx avg `0.0134` n `6`; index avg `-0.0018` n `25`; metal avg `-0.0039` n `20`; unknown avg `0.2426` n `794`
- 4h: commodity avg `0.0207` n `12`; crypto_alt avg `0.9206` n `230`; crypto_major avg `1.3269` n `8`; equity avg `0.0331` n `121`; fx avg `0.0311` n `6`; index avg `-0.0014` n `25`; metal avg `0.0153` n `20`; unknown avg `1.3366` n `794`
- 24h: commodity avg `-0.0876` n `12`; crypto_alt avg `1.36` n `230`; crypto_major avg `4.0373` n `8`; equity avg `-0.4062` n `121`; fx avg `0.0494` n `6`; index avg `-0.0522` n `25`; metal avg `-0.1362` n `20`; unknown avg `3.0256` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
