# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T03:22:25.031444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.2` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.009` n `12`; crypto_alt avg `0.0635` n `232`; crypto_major avg `0.0082` n `8`; equity avg `-0.0207` n `134`; fx avg `0.0` n `6`; index avg `0.0093` n `26`; metal avg `0.0063` n `20`; unknown avg `-0.0129` n `790`
- 1h: commodity avg `0.0268` n `12`; crypto_alt avg `0.0595` n `232`; crypto_major avg `-0.0427` n `8`; equity avg `-0.0465` n `134`; fx avg `0.0053` n `6`; index avg `0.0027` n `26`; metal avg `0.0011` n `20`; unknown avg `-0.0877` n `788`
- 4h: commodity avg `0.0281` n `12`; crypto_alt avg `0.763` n `232`; crypto_major avg `-0.0743` n `8`; equity avg `-0.1006` n `134`; fx avg `0.0045` n `6`; index avg `0.0095` n `26`; metal avg `0.0124` n `20`; unknown avg `0.9831` n `758`
- 24h: commodity avg `0.0014` n `12`; crypto_alt avg `-0.2177` n `232`; crypto_major avg `-2.0919` n `8`; equity avg `1.1314` n `134`; fx avg `-0.1243` n `6`; index avg `0.1412` n `26`; metal avg `-0.1449` n `20`; unknown avg `0.8791` n `652`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
