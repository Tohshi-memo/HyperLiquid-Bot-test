# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T00:22:25.246200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `-0.0892` n `232`; crypto_major avg `-0.2356` n `8`; equity avg `0.2153` n `134`; fx avg `-0.0073` n `6`; index avg `0.0395` n `26`; metal avg `0.0567` n `20`; unknown avg `0.7425` n `797`
- 1h: commodity avg `-0.0123` n `12`; crypto_alt avg `0.342` n `232`; crypto_major avg `-0.0508` n `8`; equity avg `0.3814` n `134`; fx avg `-0.0723` n `6`; index avg `0.0737` n `26`; metal avg `0.1325` n `20`; unknown avg `1.1056` n `795`
- 4h: commodity avg `0.0169` n `12`; crypto_alt avg `0.0633` n `232`; crypto_major avg `-0.1415` n `8`; equity avg `0.1754` n `134`; fx avg `-0.1071` n `6`; index avg `0.007` n `26`; metal avg `0.1431` n `20`; unknown avg `12.418` n `780`
- 24h: commodity avg `0.2434` n `12`; crypto_alt avg `-0.5383` n `232`; crypto_major avg `-1.5703` n `8`; equity avg `0.4981` n `134`; fx avg `-0.2176` n `6`; index avg `0.096` n `26`; metal avg `0.2292` n `20`; unknown avg `7766.6051` n `644`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
