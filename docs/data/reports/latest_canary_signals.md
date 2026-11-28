# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T23:22:30.069349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `13`; crypto_alt avg `0.0268` n `239`; crypto_major avg `0.0295` n `8`; equity avg `0.0393` n `168`; fx avg `0.0097` n `6`; index avg `0.0005` n `27`; metal avg `-0.0091` n `20`; unknown avg `0.5298` n `1266`
- 1h: commodity avg `-0.0009` n `13`; crypto_alt avg `0.1482` n `239`; crypto_major avg `0.2343` n `8`; equity avg `0.0936` n `168`; fx avg `0.0195` n `6`; index avg `0.0103` n `27`; metal avg `-0.0166` n `20`; unknown avg `0.4711` n `1240`
- 4h: commodity avg `0.1343` n `13`; crypto_alt avg `0.1126` n `239`; crypto_major avg `0.3191` n `8`; equity avg `0.1701` n `168`; fx avg `0.0086` n `6`; index avg `0.0209` n `27`; metal avg `0.0156` n `20`; unknown avg `0.0912` n `1166`
- 24h: commodity avg `0.089` n `13`; crypto_alt avg `-3.0869` n `239`; crypto_major avg `-0.599` n `8`; equity avg `0.1083` n `168`; fx avg `0.0117` n `6`; index avg `0.0105` n `27`; metal avg `0.0255` n `20`; unknown avg `0.3099` n `1067`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
