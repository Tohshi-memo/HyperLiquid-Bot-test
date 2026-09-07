# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T02:22:24.630514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0123` n `12`; crypto_alt avg `0.252` n `232`; crypto_major avg `0.2792` n `8`; equity avg `-0.0162` n `134`; fx avg `0.0098` n `6`; index avg `-0.0002` n `26`; metal avg `0.0027` n `20`; unknown avg `0.7652` n `794`
- 1h: commodity avg `0.0088` n `12`; crypto_alt avg `-0.1581` n `232`; crypto_major avg `0.015` n `8`; equity avg `0.079` n `134`; fx avg `0.0942` n `6`; index avg `0.015` n `26`; metal avg `0.0886` n `20`; unknown avg `128.3778` n `792`
- 4h: commodity avg `-0.0225` n `12`; crypto_alt avg `-0.1257` n `232`; crypto_major avg `0.1666` n `8`; equity avg `0.1419` n `134`; fx avg `-0.0341` n `6`; index avg `0.0156` n `26`; metal avg `-0.0624` n `20`; unknown avg `1.9376` n `783`
- 24h: commodity avg `-0.0252` n `12`; crypto_alt avg `0.0264` n `232`; crypto_major avg `0.0965` n `8`; equity avg `0.316` n `134`; fx avg `0.0042` n `6`; index avg `0.0213` n `26`; metal avg `-0.1262` n `20`; unknown avg `152.1011` n `678`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1964`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
