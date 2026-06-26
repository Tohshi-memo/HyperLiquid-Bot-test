# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T09:56:43.580498+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0234` n `12`; crypto_alt avg `-0.578` n `228`; crypto_major avg `-0.5461` n `8`; equity avg `-0.0009` n `86`; fx avg `-0.005` n `6`; index avg `0.004` n `23`; metal avg `-0.0517` n `20`; unknown avg `0.0225` n `765`
- 1h: commodity avg `-0.0532` n `12`; crypto_alt avg `-0.5761` n `228`; crypto_major avg `-0.8865` n `8`; equity avg `-0.0308` n `86`; fx avg `-0.0083` n `6`; index avg `-0.0095` n `23`; metal avg `0.182` n `20`; unknown avg `-0.0796` n `765`
- 4h: commodity avg `-0.3646` n `12`; crypto_alt avg `0.2719` n `228`; crypto_major avg `0.2617` n `8`; equity avg `0.1534` n `86`; fx avg `-0.0169` n `6`; index avg `0.0478` n `23`; metal avg `0.6847` n `20`; unknown avg `0.1262` n `733`
- 24h: commodity avg `-0.0106` n `12`; crypto_alt avg `-2.1476` n `228`; crypto_major avg `-2.38` n `8`; equity avg `-4.067` n `86`; fx avg `0.0112` n `6`; index avg `-0.5954` n `23`; metal avg `0.5369` n `20`; unknown avg `0.7497` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.267`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2135`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
