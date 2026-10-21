# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T00:37:36.278167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0174` n `13`; crypto_alt avg `0.1033` n `237`; crypto_major avg `0.0619` n `8`; equity avg `0.198` n `151`; fx avg `-0.0019` n `6`; index avg `0.0306` n `26`; metal avg `-0.0051` n `20`; unknown avg `-0.2134` n `1199`
- 1h: commodity avg `0.0178` n `13`; crypto_alt avg `0.3819` n `237`; crypto_major avg `0.3773` n `8`; equity avg `0.6189` n `151`; fx avg `-0.0134` n `6`; index avg `0.078` n `26`; metal avg `0.0324` n `20`; unknown avg `-0.2616` n `1191`
- 4h: commodity avg `0.1026` n `13`; crypto_alt avg `0.3714` n `237`; crypto_major avg `0.3439` n `8`; equity avg `1.5483` n `151`; fx avg `-0.0266` n `6`; index avg `0.1841` n `26`; metal avg `0.0052` n `20`; unknown avg `0.7116` n `1079`
- 24h: commodity avg `-0.0029` n `13`; crypto_alt avg `2.9721` n `237`; crypto_major avg `2.187` n `8`; equity avg `2.5508` n `151`; fx avg `0.0251` n `6`; index avg `0.3274` n `26`; metal avg `0.1051` n `20`; unknown avg `211.8625` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1663`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
