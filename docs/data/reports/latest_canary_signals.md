# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T22:07:30.241014+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `12`; crypto_alt avg `0.0664` n `230`; crypto_major avg `-0.3012` n `8`; equity avg `-0.0959` n `121`; fx avg `-0.0163` n `6`; index avg `-0.0081` n `25`; metal avg `0.0049` n `20`; unknown avg `0.0776` n `793`
- 1h: commodity avg `-0.003` n `12`; crypto_alt avg `0.3971` n `230`; crypto_major avg `-0.0796` n `8`; equity avg `-0.0395` n `121`; fx avg `-0.0268` n `6`; index avg `-0.0135` n `25`; metal avg `0.0052` n `20`; unknown avg `0.0781` n `793`
- 4h: commodity avg `0.1114` n `12`; crypto_alt avg `0.4881` n `230`; crypto_major avg `-0.4322` n `8`; equity avg `0.4765` n `121`; fx avg `-0.0203` n `6`; index avg `0.0197` n `25`; metal avg `0.0527` n `20`; unknown avg `-0.2662` n `792`
- 24h: commodity avg `0.3671` n `12`; crypto_alt avg `4.153` n `230`; crypto_major avg `3.9794` n `8`; equity avg `-0.9968` n `121`; fx avg `0.2034` n `6`; index avg `-0.1178` n `25`; metal avg `0.071` n `20`; unknown avg `2.6925` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2203`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1794`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
