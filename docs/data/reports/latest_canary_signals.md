# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T09:22:24.265553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.014` n `12`; crypto_alt avg `-0.0722` n `230`; crypto_major avg `-0.054` n `8`; equity avg `0.0234` n `92`; fx avg `0.0038` n `6`; index avg `0.0014` n `25`; metal avg `-0.0007` n `20`; unknown avg `0.0014` n `761`
- 1h: commodity avg `0.0266` n `12`; crypto_alt avg `0.1228` n `230`; crypto_major avg `0.0725` n `8`; equity avg `-0.0115` n `92`; fx avg `-0.0012` n `6`; index avg `-0.0011` n `25`; metal avg `0.005` n `20`; unknown avg `0.0439` n `761`
- 4h: commodity avg `0.1035` n `12`; crypto_alt avg `0.1548` n `230`; crypto_major avg `0.1503` n `8`; equity avg `0.1345` n `92`; fx avg `0.0014` n `6`; index avg `0.0053` n `25`; metal avg `0.0006` n `20`; unknown avg `0.0279` n `729`
- 24h: commodity avg `-0.0964` n `12`; crypto_alt avg `0.3515` n `229`; crypto_major avg `-0.4659` n `8`; equity avg `0.127` n `92`; fx avg `-0.0834` n `6`; index avg `0.1473` n `25`; metal avg `0.1827` n `20`; unknown avg `3.0129` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
