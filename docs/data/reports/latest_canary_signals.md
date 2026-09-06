# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T19:37:37.995341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `0.0651` n `232`; crypto_major avg `0.0274` n `8`; equity avg `0.0017` n `134`; fx avg `-0.0005` n `6`; index avg `-0.0047` n `26`; metal avg `-0.0005` n `20`; unknown avg `1.3957` n `793`
- 1h: commodity avg `0.0011` n `12`; crypto_alt avg `-0.195` n `232`; crypto_major avg `-0.3035` n `8`; equity avg `0.0424` n `134`; fx avg `0.0089` n `6`; index avg `-0.0014` n `26`; metal avg `0.0177` n `20`; unknown avg `1.7692` n `775`
- 4h: commodity avg `-0.0132` n `12`; crypto_alt avg `0.3692` n `232`; crypto_major avg `0.0094` n `8`; equity avg `0.2032` n `134`; fx avg `-0.0047` n `6`; index avg `0.0088` n `26`; metal avg `0.0186` n `20`; unknown avg `1.1555` n `754`
- 24h: commodity avg `0.0475` n `12`; crypto_alt avg `1.0884` n `232`; crypto_major avg `-0.1089` n `8`; equity avg `0.3708` n `134`; fx avg `-0.0064` n `6`; index avg `-0.0051` n `26`; metal avg `-0.021` n `20`; unknown avg `104.6335` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
