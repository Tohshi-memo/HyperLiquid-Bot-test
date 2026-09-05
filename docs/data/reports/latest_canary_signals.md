# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T12:07:27.415866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0158` n `12`; crypto_alt avg `0.0363` n `232`; crypto_major avg `0.075` n `8`; equity avg `-0.0072` n `134`; fx avg `0.0006` n `6`; index avg `-0.0008` n `26`; metal avg `0.0026` n `20`; unknown avg `0.0173` n `789`
- 1h: commodity avg `0.0193` n `12`; crypto_alt avg `-0.0303` n `232`; crypto_major avg `0.0692` n `8`; equity avg `0.0257` n `134`; fx avg `-0.0047` n `6`; index avg `0.0028` n `26`; metal avg `0.005` n `20`; unknown avg `-0.0171` n `787`
- 4h: commodity avg `0.0205` n `12`; crypto_alt avg `0.3523` n `232`; crypto_major avg `0.3824` n `8`; equity avg `0.1008` n `134`; fx avg `-0.0113` n `6`; index avg `0.0293` n `26`; metal avg `-0.0024` n `20`; unknown avg `-0.0804` n `780`
- 24h: commodity avg `0.2417` n `12`; crypto_alt avg `0.6032` n `232`; crypto_major avg `-1.1781` n `8`; equity avg `0.9707` n `134`; fx avg `-0.092` n `6`; index avg `0.0874` n `26`; metal avg `-0.142` n `20`; unknown avg `17.1022` n `650`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
