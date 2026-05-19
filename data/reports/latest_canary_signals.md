# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T14:52:21.848780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2789` n `12`; crypto_alt avg `-0.3551` n `228`; crypto_major avg `-0.188` n `8`; equity avg `-0.014` n `66`; fx avg `0.0168` n `6`; index avg `-0.0197` n `23`; metal avg `-0.1054` n `18`; unknown avg `0.0268` n `383`
- 1h: commodity avg `-0.0222` n `12`; crypto_alt avg `-1.1531` n `228`; crypto_major avg `-0.9364` n `8`; equity avg `-0.9078` n `66`; fx avg `0.0127` n `6`; index avg `-0.5115` n `23`; metal avg `-0.4369` n `18`; unknown avg `-0.0879` n `383`
- 4h: commodity avg `0.1602` n `12`; crypto_alt avg `-0.7459` n `228`; crypto_major avg `-0.6483` n `8`; equity avg `-0.8217` n `66`; fx avg `-0.0325` n `6`; index avg `-0.7389` n `23`; metal avg `-1.3873` n `18`; unknown avg `-0.5945` n `383`
- 24h: commodity avg `0.9867` n `12`; crypto_alt avg `0.3862` n `228`; crypto_major avg `0.3583` n `8`; equity avg `-1.4104` n `66`; fx avg `0.2295` n `6`; index avg `-1.3609` n `23`; metal avg `-2.0052` n `18`; unknown avg `-0.367` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.2393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
