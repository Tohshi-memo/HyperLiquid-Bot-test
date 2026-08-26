# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T07:22:26.976798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `0.012` n `231`; crypto_major avg `-0.014` n `8`; equity avg `-0.0759` n `122`; fx avg `0.0008` n `6`; index avg `-0.0087` n `25`; metal avg `0.0098` n `20`; unknown avg `0.0219` n `797`
- 1h: commodity avg `-0.08` n `12`; crypto_alt avg `0.0664` n `231`; crypto_major avg `0.2322` n `8`; equity avg `0.0156` n `122`; fx avg `-0.0008` n `6`; index avg `0.006` n `25`; metal avg `-0.0162` n `20`; unknown avg `0.1396` n `797`
- 4h: commodity avg `0.0753` n `12`; crypto_alt avg `-0.0894` n `231`; crypto_major avg `0.0843` n `8`; equity avg `-0.2275` n `122`; fx avg `-0.0405` n `6`; index avg `-0.0204` n `25`; metal avg `-0.1316` n `20`; unknown avg `0.148` n `781`
- 24h: commodity avg `-0.613` n `12`; crypto_alt avg `-2.4005` n `231`; crypto_major avg `-2.4472` n `8`; equity avg `0.5303` n `122`; fx avg `-0.0346` n `6`; index avg `0.0864` n `25`; metal avg `0.0885` n `20`; unknown avg `0.8633` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
