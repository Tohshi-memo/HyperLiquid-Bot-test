# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T13:07:25.560009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0637` n `12`; crypto_alt avg `-0.2848` n `230`; crypto_major avg `-0.3457` n `8`; equity avg `-0.3059` n `109`; fx avg `0.0016` n `6`; index avg `-0.0422` n `25`; metal avg `-0.0605` n `20`; unknown avg `-0.183` n `781`
- 1h: commodity avg `0.2582` n `12`; crypto_alt avg `-0.207` n `230`; crypto_major avg `-0.4604` n `8`; equity avg `-0.4959` n `109`; fx avg `0.0034` n `6`; index avg `-0.0395` n `25`; metal avg `-0.2104` n `20`; unknown avg `-0.1453` n `781`
- 4h: commodity avg `0.2524` n `12`; crypto_alt avg `-0.5819` n `230`; crypto_major avg `-1.0292` n `8`; equity avg `-0.5975` n `109`; fx avg `-0.0058` n `6`; index avg `-0.0669` n `25`; metal avg `-0.2674` n `20`; unknown avg `108.0317` n `781`
- 24h: commodity avg `0.1762` n `12`; crypto_alt avg `-0.1741` n `230`; crypto_major avg `-1.1304` n `8`; equity avg `-2.1934` n `109`; fx avg `0.0043` n `6`; index avg `-0.4908` n `25`; metal avg `0.2119` n `20`; unknown avg `113.1005` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
