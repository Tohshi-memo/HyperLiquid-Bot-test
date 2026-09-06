# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T06:37:28.413973+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0123` n `12`; crypto_alt avg `-0.0822` n `232`; crypto_major avg `-0.1154` n `8`; equity avg `-0.0013` n `134`; fx avg `-0.0044` n `6`; index avg `-0.0082` n `26`; metal avg `-0.0051` n `20`; unknown avg `-0.0108` n `790`
- 1h: commodity avg `0.0218` n `12`; crypto_alt avg `-0.5365` n `232`; crypto_major avg `-0.4135` n `8`; equity avg `0.045` n `134`; fx avg `-0.0204` n `6`; index avg `0.0034` n `26`; metal avg `-0.001` n `20`; unknown avg `0.1447` n `772`
- 4h: commodity avg `0.0158` n `12`; crypto_alt avg `-0.239` n `232`; crypto_major avg `0.3353` n `8`; equity avg `0.1195` n `134`; fx avg `0.0051` n `6`; index avg `0.0217` n `26`; metal avg `0.0038` n `20`; unknown avg `462.9897` n `728`
- 24h: commodity avg `0.1761` n `12`; crypto_alt avg `1.9653` n `232`; crypto_major avg `2.736` n `8`; equity avg `0.4523` n `134`; fx avg `-0.0422` n `6`; index avg `0.0726` n `26`; metal avg `0.0027` n `20`; unknown avg `494.4563` n `676`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
