# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T17:52:21.075810+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1135` n `12`; crypto_alt avg `0.0029` n `228`; crypto_major avg `-0.1013` n `8`; equity avg `-0.2521` n `66`; fx avg `-0.0055` n `6`; index avg `-0.1557` n `23`; metal avg `-0.0758` n `18`; unknown avg `-0.0081` n `383`
- 1h: commodity avg `-0.054` n `12`; crypto_alt avg `-0.0194` n `228`; crypto_major avg `-0.0181` n `8`; equity avg `0.2739` n `66`; fx avg `0.0344` n `6`; index avg `0.0618` n `23`; metal avg `-0.0859` n `18`; unknown avg `0.2302` n `383`
- 4h: commodity avg `-0.0386` n `12`; crypto_alt avg `-0.4757` n `228`; crypto_major avg `-0.2498` n `8`; equity avg `1.067` n `66`; fx avg `-0.0466` n `6`; index avg `0.456` n `23`; metal avg `-0.1347` n `18`; unknown avg `-0.0316` n `383`
- 24h: commodity avg `0.4071` n `12`; crypto_alt avg `0.7647` n `228`; crypto_major avg `0.8004` n `8`; equity avg `0.8856` n `66`; fx avg `-0.0094` n `6`; index avg `-0.1085` n `23`; metal avg `-1.9042` n `18`; unknown avg `0.0914` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
