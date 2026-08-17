# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T02:07:27.114567+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.074` n `12`; crypto_alt avg `-0.069` n `230`; crypto_major avg `-0.1075` n `8`; equity avg `-0.0228` n `114`; fx avg `0.0076` n `6`; index avg `-0.0029` n `25`; metal avg `0.0056` n `20`; unknown avg `0.0751` n `792`
- 1h: commodity avg `0.1704` n `12`; crypto_alt avg `-0.0077` n `230`; crypto_major avg `0.0746` n `8`; equity avg `-0.0964` n `114`; fx avg `0.0157` n `6`; index avg `-0.01` n `25`; metal avg `-0.0489` n `20`; unknown avg `-0.1141` n `792`
- 4h: commodity avg `0.0061` n `12`; crypto_alt avg `0.526` n `230`; crypto_major avg `0.5711` n `8`; equity avg `0.0814` n `114`; fx avg `-0.024` n `6`; index avg `-0.0034` n `25`; metal avg `0.2612` n `20`; unknown avg `0.0544` n `791`
- 24h: commodity avg `-0.0553` n `12`; crypto_alt avg `-0.0103` n `230`; crypto_major avg `0.2489` n `8`; equity avg `0.3314` n `114`; fx avg `-0.0519` n `6`; index avg `0.0367` n `25`; metal avg `0.2287` n `20`; unknown avg `-0.0504` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1988`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
