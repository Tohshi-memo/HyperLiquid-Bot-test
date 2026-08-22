# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T23:32:22.771510+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `-0.1265` n `230`; crypto_major avg `-0.1078` n `8`; equity avg `0.0264` n `121`; fx avg `0.0069` n `6`; index avg `0.0029` n `25`; metal avg `-0.0043` n `20`; unknown avg `-0.0221` n `794`
- 1h: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.1913` n `230`; crypto_major avg `-0.3736` n `8`; equity avg `0.0514` n `121`; fx avg `0.0249` n `6`; index avg `0.013` n `25`; metal avg `-0.0153` n `20`; unknown avg `0.0919` n `794`
- 4h: commodity avg `0.0911` n `12`; crypto_alt avg `-1.2431` n `230`; crypto_major avg `-0.947` n `8`; equity avg `0.0877` n `121`; fx avg `0.0483` n `6`; index avg `0.0086` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.2231` n `794`
- 24h: commodity avg `0.0615` n `12`; crypto_alt avg `-2.2132` n `230`; crypto_major avg `-0.2373` n `8`; equity avg `-0.3776` n `121`; fx avg `0.1152` n `6`; index avg `-0.0578` n `25`; metal avg `-0.0746` n `20`; unknown avg `2.9929` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
