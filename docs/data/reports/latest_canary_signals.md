# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T23:37:25.247242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0053` n `12`; crypto_alt avg `0.0829` n `232`; crypto_major avg `-0.0161` n `8`; equity avg `0.0939` n `134`; fx avg `0.0047` n `6`; index avg `0.0097` n `26`; metal avg `0.043` n `20`; unknown avg `0.5091` n `797`
- 1h: commodity avg `0.0147` n `12`; crypto_alt avg `0.3379` n `232`; crypto_major avg `0.2512` n `8`; equity avg `0.0046` n `134`; fx avg `-0.0243` n `6`; index avg `-0.0199` n `26`; metal avg `0.0689` n `20`; unknown avg `0.4518` n `795`
- 4h: commodity avg `0.0378` n `12`; crypto_alt avg `-0.3231` n `232`; crypto_major avg `-0.3219` n `8`; equity avg `-0.1229` n `134`; fx avg `-0.0285` n `6`; index avg `-0.0546` n `26`; metal avg `0.0691` n `20`; unknown avg `1.5986` n `752`
- 24h: commodity avg `0.2116` n `12`; crypto_alt avg `-0.6023` n `232`; crypto_major avg `-1.6986` n `8`; equity avg `0.402` n `134`; fx avg `-0.1998` n `6`; index avg `0.0595` n `26`; metal avg `0.134` n `20`; unknown avg `7789.1443` n `642`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
