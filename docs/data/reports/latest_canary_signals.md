# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T19:52:22.026877+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0056` n `12`; crypto_alt avg `0.0529` n `232`; crypto_major avg `0.0113` n `8`; equity avg `0.0133` n `134`; fx avg `0.0028` n `6`; index avg `0.0063` n `26`; metal avg `-0.0058` n `20`; unknown avg `-0.1586` n `793`
- 1h: commodity avg `-0.0183` n `12`; crypto_alt avg `-0.042` n `232`; crypto_major avg `-0.1215` n `8`; equity avg `0.0584` n `134`; fx avg `0.0106` n `6`; index avg `0.0051` n `26`; metal avg `0.0102` n `20`; unknown avg `148.2633` n `775`
- 4h: commodity avg `-0.0339` n `12`; crypto_alt avg `0.1939` n `232`; crypto_major avg `0.0407` n `8`; equity avg `0.1965` n `134`; fx avg `0.0012` n `6`; index avg `0.0203` n `26`; metal avg `0.016` n `20`; unknown avg `0.3572` n `755`
- 24h: commodity avg `-0.0004` n `12`; crypto_alt avg `1.1782` n `232`; crypto_major avg `-0.0029` n `8`; equity avg `0.3973` n `134`; fx avg `0.0036` n `6`; index avg `0.0087` n `26`; metal avg `-0.0222` n `20`; unknown avg `104.6001` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1652`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
