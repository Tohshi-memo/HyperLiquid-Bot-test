# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T12:22:26.105152+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0407` n `12`; crypto_alt avg `0.0902` n `232`; crypto_major avg `0.2143` n `8`; equity avg `0.0534` n `134`; fx avg `-0.0038` n `6`; index avg `-0.0008` n `26`; metal avg `-0.0018` n `20`; unknown avg `222.3459` n `792`
- 1h: commodity avg `-0.0111` n `12`; crypto_alt avg `0.1059` n `232`; crypto_major avg `0.2114` n `8`; equity avg `0.0514` n `134`; fx avg `-0.0248` n `6`; index avg `-0.0055` n `26`; metal avg `0.0012` n `20`; unknown avg `222.7367` n `790`
- 4h: commodity avg `-0.0083` n `12`; crypto_alt avg `0.8476` n `232`; crypto_major avg `0.5346` n `8`; equity avg `0.2178` n `134`; fx avg `-0.0024` n `6`; index avg `0.018` n `26`; metal avg `0.0075` n `20`; unknown avg `387.7228` n `784`
- 24h: commodity avg `0.1021` n `12`; crypto_alt avg `2.3197` n `232`; crypto_major avg `2.1909` n `8`; equity avg `0.5676` n `134`; fx avg `-0.0221` n `6`; index avg `0.076` n `26`; metal avg `0.0073` n `20`; unknown avg `491.8718` n `678`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
