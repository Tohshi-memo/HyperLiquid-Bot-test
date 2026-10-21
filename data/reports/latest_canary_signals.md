# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T00:52:31.952965+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0311` n `13`; crypto_alt avg `0.072` n `237`; crypto_major avg `0.0962` n `8`; equity avg `-0.0914` n `151`; fx avg `0.0083` n `6`; index avg `-0.0443` n `26`; metal avg `-0.0043` n `20`; unknown avg `0.6614` n `1199`
- 1h: commodity avg `-0.0127` n `13`; crypto_alt avg `0.338` n `237`; crypto_major avg `0.3512` n `8`; equity avg `0.3496` n `151`; fx avg `0.0131` n `6`; index avg `0.006` n `26`; metal avg `0.0237` n `20`; unknown avg `0.4984` n `1191`
- 4h: commodity avg `0.0152` n `13`; crypto_alt avg `0.4633` n `237`; crypto_major avg `0.4476` n `8`; equity avg `1.125` n `151`; fx avg `-0.0159` n `6`; index avg `0.0851` n `26`; metal avg `-0.0139` n `20`; unknown avg `0.4377` n `1079`
- 24h: commodity avg `-0.0251` n `13`; crypto_alt avg `3.0169` n `237`; crypto_major avg `2.2842` n `8`; equity avg `2.8228` n `151`; fx avg `0.0578` n `6`; index avg `0.3611` n `26`; metal avg `0.1438` n `20`; unknown avg `212.4676` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
