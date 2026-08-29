# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T10:22:24.510629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `0.1616` n `231`; crypto_major avg `0.2362` n `8`; equity avg `0.0177` n `127`; fx avg `-0.0021` n `6`; index avg `0.0031` n `26`; metal avg `0.0005` n `20`; unknown avg `0.0339` n `793`
- 1h: commodity avg `0.0142` n `12`; crypto_alt avg `0.1539` n `231`; crypto_major avg `0.1616` n `8`; equity avg `0.0215` n `127`; fx avg `-0.0175` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0053` n `20`; unknown avg `0.0286` n `791`
- 4h: commodity avg `0.0556` n `12`; crypto_alt avg `-0.0145` n `231`; crypto_major avg `0.3473` n `8`; equity avg `0.0683` n `127`; fx avg `-0.0124` n `6`; index avg `-0.0094` n `26`; metal avg `0.0123` n `20`; unknown avg `0.0622` n `791`
- 24h: commodity avg `-0.0527` n `12`; crypto_alt avg `-1.7437` n `231`; crypto_major avg `-1.6198` n `8`; equity avg `-1.3247` n `127`; fx avg `-0.0326` n `6`; index avg `-0.1343` n `26`; metal avg `-0.6958` n `20`; unknown avg `-0.3747` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
