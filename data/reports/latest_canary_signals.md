# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T17:22:26.479233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0172` n `12`; crypto_alt avg `-0.0074` n `232`; crypto_major avg `0.0715` n `8`; equity avg `-0.0022` n `134`; fx avg `-0.0038` n `6`; index avg `-0.0015` n `26`; metal avg `0.0072` n `20`; unknown avg `-0.1849` n `785`
- 1h: commodity avg `0.0032` n `12`; crypto_alt avg `-0.1497` n `232`; crypto_major avg `0.0662` n `8`; equity avg `0.0209` n `134`; fx avg `-0.0185` n `6`; index avg `0.0002` n `26`; metal avg `-0.0048` n `20`; unknown avg `147.6241` n `777`
- 4h: commodity avg `0.0308` n `12`; crypto_alt avg `-0.2145` n `232`; crypto_major avg `-0.3534` n `8`; equity avg `-0.1213` n `134`; fx avg `-0.016` n `6`; index avg `-0.03` n `26`; metal avg `-0.0244` n `20`; unknown avg `151.1612` n `760`
- 24h: commodity avg `0.115` n `12`; crypto_alt avg `1.1282` n `232`; crypto_major avg `0.0922` n `8`; equity avg `0.1927` n `134`; fx avg `-0.037` n `6`; index avg `0.0113` n `26`; metal avg `-0.0386` n `20`; unknown avg `1.6352` n `664`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
