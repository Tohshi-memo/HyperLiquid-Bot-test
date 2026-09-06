# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T06:52:25.961870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `0.2005` n `232`; crypto_major avg `0.0082` n `8`; equity avg `0.0183` n `134`; fx avg `-0.0029` n `6`; index avg `0.002` n `26`; metal avg `0.0027` n `20`; unknown avg `0.0158` n `792`
- 1h: commodity avg `-0.0031` n `12`; crypto_alt avg `-0.2817` n `232`; crypto_major avg `-0.3833` n `8`; equity avg `0.0386` n `134`; fx avg `-0.0121` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0064` n `20`; unknown avg `0.1908` n `772`
- 4h: commodity avg `0.023` n `12`; crypto_alt avg `0.0542` n `232`; crypto_major avg `0.3141` n `8`; equity avg `0.1264` n `134`; fx avg `0.0023` n `6`; index avg `0.0049` n `26`; metal avg `0.0118` n `20`; unknown avg `462.9165` n `728`
- 24h: commodity avg `0.1442` n `12`; crypto_alt avg `2.1148` n `232`; crypto_major avg `2.6565` n `8`; equity avg `0.4542` n `134`; fx avg `-0.0431` n `6`; index avg `0.0896` n `26`; metal avg `0.0085` n `20`; unknown avg `493.4049` n `676`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
