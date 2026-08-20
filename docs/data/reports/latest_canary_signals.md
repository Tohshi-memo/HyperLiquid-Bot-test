# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T22:12:16.967483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `12`; crypto_alt avg `0.0434` n `230`; crypto_major avg `-0.3963` n `8`; equity avg `-0.0969` n `121`; fx avg `-0.017` n `6`; index avg `-0.0109` n `25`; metal avg `0.0041` n `20`; unknown avg `0.1268` n `793`
- 1h: commodity avg `-0.0066` n `12`; crypto_alt avg `0.3733` n `230`; crypto_major avg `-0.175` n `8`; equity avg `-0.0405` n `121`; fx avg `-0.0275` n `6`; index avg `-0.0163` n `25`; metal avg `0.0043` n `20`; unknown avg `0.0973` n `793`
- 4h: commodity avg `0.1078` n `12`; crypto_alt avg `0.4639` n `230`; crypto_major avg `-0.5279` n `8`; equity avg `0.4756` n `121`; fx avg `-0.021` n `6`; index avg `0.0168` n `25`; metal avg `0.0519` n `20`; unknown avg `-0.2449` n `792`
- 24h: commodity avg `0.3635` n `12`; crypto_alt avg `4.1321` n `230`; crypto_major avg `3.8806` n `8`; equity avg `-0.9978` n `121`; fx avg `0.2027` n `6`; index avg `-0.1207` n `25`; metal avg `0.0702` n `20`; unknown avg `2.6861` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2203`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1793`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
