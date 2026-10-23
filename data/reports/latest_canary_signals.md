# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T22:07:28.192270+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0342` n `13`; crypto_alt avg `0.215` n `237`; crypto_major avg `0.1051` n `8`; equity avg `0.0019` n `152`; fx avg `0.0037` n `6`; index avg `-0.0038` n `26`; metal avg `-0.0029` n `20`; unknown avg `0.1594` n `1220`
- 1h: commodity avg `0.1232` n `13`; crypto_alt avg `-0.1105` n `237`; crypto_major avg `-0.0498` n `8`; equity avg `-0.0452` n `152`; fx avg `0.0172` n `6`; index avg `-0.0125` n `26`; metal avg `-0.0051` n `20`; unknown avg `-0.2558` n `1220`
- 4h: commodity avg `0.1896` n `13`; crypto_alt avg `-0.9135` n `237`; crypto_major avg `-0.3509` n `8`; equity avg `-0.294` n `152`; fx avg `0.0065` n `6`; index avg `-0.0153` n `26`; metal avg `-0.0587` n `20`; unknown avg `-0.3511` n `1133`
- 24h: commodity avg `0.5414` n `13`; crypto_alt avg `0.1413` n `237`; crypto_major avg `0.255` n `8`; equity avg `1.2899` n `152`; fx avg `-0.0634` n `6`; index avg `0.0704` n `26`; metal avg `-0.1717` n `20`; unknown avg `-0.5495` n `1012`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1995`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
