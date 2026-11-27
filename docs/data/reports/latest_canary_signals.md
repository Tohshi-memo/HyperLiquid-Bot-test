# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T08:37:33.960238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0588` n `13`; crypto_alt avg `-0.1904` n `239`; crypto_major avg `-0.3985` n `8`; equity avg `-0.1358` n `168`; fx avg `0.0235` n `6`; index avg `-0.0013` n `27`; metal avg `-0.0771` n `20`; unknown avg `0.5985` n `1251`
- 1h: commodity avg `-0.103` n `13`; crypto_alt avg `0.0758` n `239`; crypto_major avg `0.1004` n `8`; equity avg `0.4747` n `168`; fx avg `-0.026` n `6`; index avg `0.0407` n `27`; metal avg `0.0277` n `20`; unknown avg `1.3205` n `1171`
- 4h: commodity avg `-0.1322` n `13`; crypto_alt avg `0.1531` n `239`; crypto_major avg `0.2373` n `8`; equity avg `0.6922` n `168`; fx avg `-0.0525` n `6`; index avg `-0.011` n `27`; metal avg `0.3566` n `20`; unknown avg `0.8006` n `1153`
- 24h: commodity avg `0.3074` n `13`; crypto_alt avg `2.0285` n `239`; crypto_major avg `2.579` n `8`; equity avg `3.9769` n `168`; fx avg `-0.0711` n `6`; index avg `0.3093` n `27`; metal avg `1.2205` n `20`; unknown avg `210.8267` n `1043`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
