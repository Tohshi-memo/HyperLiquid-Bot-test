# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T13:07:25.771378+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `12`; crypto_alt avg `-0.1182` n `232`; crypto_major avg `0.0299` n `8`; equity avg `0.016` n `133`; fx avg `0.0116` n `6`; index avg `0.0017` n `26`; metal avg `-0.0048` n `20`; unknown avg `13.5412` n `790`
- 1h: commodity avg `-0.2054` n `12`; crypto_alt avg `0.1998` n `232`; crypto_major avg `0.5569` n `8`; equity avg `0.4832` n `133`; fx avg `-0.0265` n `6`; index avg `0.109` n `26`; metal avg `0.2908` n `20`; unknown avg `14.0915` n `790`
- 4h: commodity avg `0.0518` n `12`; crypto_alt avg `0.404` n `232`; crypto_major avg `0.7758` n `8`; equity avg `0.228` n `133`; fx avg `-0.1052` n `6`; index avg `0.0482` n `26`; metal avg `0.2433` n `20`; unknown avg `2.241` n `790`
- 24h: commodity avg `0.5707` n `12`; crypto_alt avg `2.3177` n `232`; crypto_major avg `2.5858` n `8`; equity avg `1.5575` n `133`; fx avg `-0.3994` n `6`; index avg `0.1629` n `26`; metal avg `0.8434` n `20`; unknown avg `0.0626` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0408`, n `668`, weak_sample_signal
