# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T08:07:30.281414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0604` n `13`; crypto_alt avg `0.1236` n `239`; crypto_major avg `0.1953` n `8`; equity avg `0.2816` n `168`; fx avg `-0.0062` n `6`; index avg `0.0198` n `27`; metal avg `-0.0443` n `20`; unknown avg `0.6023` n `1213`
- 1h: commodity avg `-0.1321` n `13`; crypto_alt avg `-0.0469` n `239`; crypto_major avg `0.0666` n `8`; equity avg `-0.1552` n `168`; fx avg `-0.015` n `6`; index avg `-0.032` n `27`; metal avg `-0.0329` n `20`; unknown avg `35.0975` n `1221`
- 4h: commodity avg `-0.0669` n `13`; crypto_alt avg `0.3533` n `239`; crypto_major avg `0.7431` n `8`; equity avg `0.7887` n `168`; fx avg `-0.0555` n `6`; index avg `-0.0078` n `27`; metal avg `0.3693` n `20`; unknown avg `0.9139` n `1199`
- 24h: commodity avg `0.4143` n `13`; crypto_alt avg `2.1876` n `239`; crypto_major avg `2.9313` n `8`; equity avg `3.654` n `168`; fx avg `-0.0718` n `6`; index avg `0.2847` n `27`; metal avg `1.2398` n `20`; unknown avg `223.4151` n `973`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
