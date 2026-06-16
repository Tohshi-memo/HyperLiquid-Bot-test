# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T08:22:47.142925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2557` n `12`; crypto_alt avg `0.2345` n `228`; crypto_major avg `0.1258` n `8`; equity avg `0.1149` n `77`; fx avg `0.0154` n `6`; index avg `0.0943` n `23`; metal avg `0.2077` n `18`; unknown avg `-0.0329` n `687`
- 1h: commodity avg `-0.5663` n `12`; crypto_alt avg `0.6329` n `228`; crypto_major avg `0.3415` n `8`; equity avg `0.2801` n `77`; fx avg `0.0246` n `6`; index avg `0.1214` n `23`; metal avg `0.4274` n `18`; unknown avg `0.0551` n `687`
- 4h: commodity avg `-0.6666` n `12`; crypto_alt avg `1.0837` n `228`; crypto_major avg `1.1432` n `8`; equity avg `0.495` n `77`; fx avg `-0.0056` n `6`; index avg `0.08` n `23`; metal avg `0.5631` n `18`; unknown avg `0.7808` n `647`
- 24h: commodity avg `-0.1888` n `12`; crypto_alt avg `1.2528` n `228`; crypto_major avg `3.0793` n `8`; equity avg `1.515` n `76`; fx avg `-0.0787` n `6`; index avg `0.489` n `23`; metal avg `0.2431` n `18`; unknown avg `0.6672` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
