# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T15:07:31.641841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0213` n `12`; crypto_alt avg `0.0989` n `232`; crypto_major avg `0.0538` n `8`; equity avg `0.1127` n `134`; fx avg `0.0231` n `6`; index avg `0.0139` n `26`; metal avg `0.0685` n `20`; unknown avg `1.0417` n `795`
- 1h: commodity avg `-0.1262` n `12`; crypto_alt avg `0.9158` n `232`; crypto_major avg `0.6907` n `8`; equity avg `0.5811` n `134`; fx avg `0.0455` n `6`; index avg `0.057` n `26`; metal avg `0.0204` n `20`; unknown avg `1.1677` n `795`
- 4h: commodity avg `-0.4052` n `12`; crypto_alt avg `0.1317` n `232`; crypto_major avg `0.2229` n `8`; equity avg `0.8272` n `134`; fx avg `0.0381` n `6`; index avg `0.0348` n `26`; metal avg `0.077` n `20`; unknown avg `0.13` n `775`
- 24h: commodity avg `-0.2778` n `12`; crypto_alt avg `0.1171` n `232`; crypto_major avg `-0.2732` n `8`; equity avg `0.7337` n `134`; fx avg `-0.0615` n `6`; index avg `-0.0243` n `26`; metal avg `0.0116` n `20`; unknown avg `7061.6594` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
