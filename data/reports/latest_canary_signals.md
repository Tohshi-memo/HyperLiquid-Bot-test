# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T08:37:18.706272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.116` n `12`; crypto_alt avg `-0.0541` n `228`; crypto_major avg `-0.0789` n `8`; equity avg `0.0791` n `66`; fx avg `-0.0036` n `5`; index avg `0.0662` n `23`; metal avg `0.0963` n `18`; unknown avg `0.0156` n `383`
- 1h: commodity avg `0.112` n `12`; crypto_alt avg `-0.0027` n `228`; crypto_major avg `-0.016` n `8`; equity avg `0.4579` n `66`; fx avg `-0.0056` n `5`; index avg `0.2103` n `23`; metal avg `0.0106` n `18`; unknown avg `-0.1897` n `383`
- 4h: commodity avg `-0.3061` n `12`; crypto_alt avg `-0.6824` n `228`; crypto_major avg `-0.4421` n `8`; equity avg `0.8392` n `66`; fx avg `-0.0753` n `5`; index avg `0.3125` n `23`; metal avg `0.4651` n `18`; unknown avg `-0.1568` n `363`
- 24h: commodity avg `0.5779` n `12`; crypto_alt avg `-2.9816` n `228`; crypto_major avg `-1.3063` n `8`; equity avg `0.569` n `65`; fx avg `0.0271` n `5`; index avg `0.3232` n `23`; metal avg `0.1585` n `18`; unknown avg `-0.3936` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
