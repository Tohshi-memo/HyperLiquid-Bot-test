# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T10:52:27.609500+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.055` n `12`; crypto_alt avg `-0.0522` n `230`; crypto_major avg `-0.0462` n `8`; equity avg `-0.1616` n `109`; fx avg `0.0043` n `6`; index avg `-0.0251` n `25`; metal avg `0.0108` n `20`; unknown avg `-0.0577` n `781`
- 1h: commodity avg `0.1141` n `12`; crypto_alt avg `-0.0605` n `230`; crypto_major avg `-0.0636` n `8`; equity avg `-0.1797` n `109`; fx avg `-0.005` n `6`; index avg `-0.0264` n `25`; metal avg `-0.0074` n `20`; unknown avg `42.2036` n `781`
- 4h: commodity avg `0.082` n `12`; crypto_alt avg `-0.4266` n `230`; crypto_major avg `-0.5993` n `8`; equity avg `-0.2273` n `109`; fx avg `-0.0339` n `6`; index avg `-0.0255` n `25`; metal avg `0.2295` n `20`; unknown avg `108.1941` n `781`
- 24h: commodity avg `-0.1557` n `12`; crypto_alt avg `0.0189` n `230`; crypto_major avg `-0.4306` n `8`; equity avg `-1.5293` n `109`; fx avg `-0.0105` n `6`; index avg `-0.3213` n `25`; metal avg `0.582` n `20`; unknown avg `113.0112` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
