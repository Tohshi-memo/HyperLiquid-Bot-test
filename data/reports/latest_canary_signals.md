# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T01:37:31.000966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0604` n `12`; crypto_alt avg `-0.0006` n `230`; crypto_major avg `-0.0291` n `8`; equity avg `-0.3114` n `94`; fx avg `-0.0001` n `6`; index avg `-0.0519` n `25`; metal avg `-0.0244` n `20`; unknown avg `0.0253` n `768`
- 1h: commodity avg `0.0702` n `12`; crypto_alt avg `0.4668` n `230`; crypto_major avg `0.4096` n `8`; equity avg `-0.0452` n `94`; fx avg `-0.025` n `6`; index avg `-0.0105` n `25`; metal avg `0.0713` n `20`; unknown avg `-0.0061` n `768`
- 4h: commodity avg `0.0717` n `12`; crypto_alt avg `-0.9034` n `230`; crypto_major avg `-0.7938` n `8`; equity avg `-1.4005` n `94`; fx avg `-0.0005` n `6`; index avg `-0.2222` n `25`; metal avg `-0.0203` n `20`; unknown avg `-0.5116` n `768`
- 24h: commodity avg `-0.0544` n `12`; crypto_alt avg `-1.4822` n `230`; crypto_major avg `-2.3498` n `8`; equity avg `-4.4242` n `94`; fx avg `-0.1693` n `6`; index avg `-0.529` n `25`; metal avg `-0.6567` n `20`; unknown avg `-0.6296` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
