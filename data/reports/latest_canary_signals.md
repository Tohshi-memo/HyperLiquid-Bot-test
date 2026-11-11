# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T09:37:31.716785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0274` n `13`; crypto_alt avg `-0.1859` n `239`; crypto_major avg `-0.1552` n `8`; equity avg `-0.0443` n `161`; fx avg `-0.0385` n `6`; index avg `0.0169` n `27`; metal avg `0.03` n `20`; unknown avg `1.942` n `1261`
- 1h: commodity avg `0.141` n `13`; crypto_alt avg `-0.3013` n `239`; crypto_major avg `-0.1031` n `8`; equity avg `-0.1432` n `161`; fx avg `-0.0583` n `6`; index avg `-0.0335` n `27`; metal avg `-0.0153` n `20`; unknown avg `1.6105` n `1239`
- 4h: commodity avg `0.1954` n `13`; crypto_alt avg `-0.7819` n `239`; crypto_major avg `-0.3732` n `8`; equity avg `0.4217` n `161`; fx avg `-0.0904` n `6`; index avg `-0.0207` n `27`; metal avg `0.0177` n `20`; unknown avg `41.5073` n `1199`
- 24h: commodity avg `0.8793` n `13`; crypto_alt avg `-1.4937` n `239`; crypto_major avg `-2.0575` n `8`; equity avg `1.7568` n `161`; fx avg `-0.2525` n `6`; index avg `0.1935` n `27`; metal avg `0.1454` n `20`; unknown avg `1.6464` n `1175`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
