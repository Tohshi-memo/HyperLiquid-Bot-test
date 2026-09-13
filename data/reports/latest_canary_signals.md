# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T09:37:27.004875+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2263` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0133` n `12`; crypto_alt avg `-0.4011` n `233`; crypto_major avg `-0.6579` n `8`; equity avg `-0.4992` n `136`; fx avg `0.0075` n `6`; index avg `-0.0913` n `27`; metal avg `-0.0231` n `20`; unknown avg `0.0522` n `830`
- 1h: commodity avg `0.0133` n `12`; crypto_alt avg `-0.4011` n `233`; crypto_major avg `-0.6579` n `8`; equity avg `-0.4992` n `136`; fx avg `0.0075` n `6`; index avg `-0.0913` n `27`; metal avg `-0.0231` n `20`; unknown avg `0.0522` n `830`
- 4h: commodity avg `0.0334` n `12`; crypto_alt avg `-1.0038` n `233`; crypto_major avg `-1.3943` n `8`; equity avg `-1.0437` n `136`; fx avg `0.0052` n `6`; index avg `-0.168` n `26`; metal avg `-0.0497` n `20`; unknown avg `0.093` n `804`
- 24h: commodity avg `0.1275` n `12`; crypto_alt avg `-0.3663` n `233`; crypto_major avg `-1.6` n `8`; equity avg `-1.5825` n `136`; fx avg `-0.0084` n `6`; index avg `-0.2582` n `26`; metal avg `-0.0188` n `20`; unknown avg `0.0912` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0854`, n `671`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0759`, n `671`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0733`, n `671`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.073`, n `671`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0662`, n `671`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0652`, n `671`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0637`, n `671`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0575`, n `671`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0558`, n `671`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0553`, n `671`, weak_sample_signal
