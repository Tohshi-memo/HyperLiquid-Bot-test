# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T13:52:25.856751+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2207` n `13`; crypto_alt avg `0.3916` n `237`; crypto_major avg `0.356` n `8`; equity avg `0.7403` n `152`; fx avg `0.016` n `6`; index avg `0.0443` n `26`; metal avg `0.0092` n `20`; unknown avg `0.0592` n `1217`
- 1h: commodity avg `0.1296` n `13`; crypto_alt avg `0.0901` n `237`; crypto_major avg `0.3506` n `8`; equity avg `0.2983` n `152`; fx avg `0.0131` n `6`; index avg `0.0442` n `26`; metal avg `-0.0025` n `20`; unknown avg `8.7738` n `1215`
- 4h: commodity avg `0.0104` n `13`; crypto_alt avg `0.1753` n `237`; crypto_major avg `0.2777` n `8`; equity avg `-0.4754` n `152`; fx avg `0.0049` n `6`; index avg `-0.0355` n `26`; metal avg `0.0404` n `20`; unknown avg `2.2562` n `1209`
- 24h: commodity avg `0.3809` n `13`; crypto_alt avg `0.5371` n `237`; crypto_major avg `0.656` n `8`; equity avg `-1.3683` n `152`; fx avg `-0.0544` n `6`; index avg `-0.2282` n `26`; metal avg `-0.2809` n `20`; unknown avg `50.3608` n `940`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
