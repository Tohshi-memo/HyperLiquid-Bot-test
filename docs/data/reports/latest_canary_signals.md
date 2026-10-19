# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T22:22:27.128575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `13`; crypto_alt avg `0.3455` n `237`; crypto_major avg `0.1189` n `8`; equity avg `0.0673` n `151`; fx avg `-0.0258` n `6`; index avg `0.0023` n `26`; metal avg `-0.0041` n `20`; unknown avg `0.0328` n `1196`
- 1h: commodity avg `-0.0281` n `13`; crypto_alt avg `0.6869` n `237`; crypto_major avg `0.3416` n `8`; equity avg `0.1246` n `151`; fx avg `-0.0161` n `6`; index avg `0.0384` n `26`; metal avg `-0.0062` n `20`; unknown avg `-0.0129` n `1184`
- 4h: commodity avg `-0.1724` n `13`; crypto_alt avg `1.2522` n `237`; crypto_major avg `0.8716` n `8`; equity avg `0.2544` n `151`; fx avg `-0.0127` n `6`; index avg `0.0447` n `26`; metal avg `-0.0754` n `20`; unknown avg `2.0529` n `1114`
- 24h: commodity avg `-0.0623` n `13`; crypto_alt avg `1.9551` n `237`; crypto_major avg `1.2021` n `8`; equity avg `1.9571` n `151`; fx avg `-0.0332` n `6`; index avg `0.3402` n `26`; metal avg `-0.1231` n `20`; unknown avg `2.757` n `980`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1946`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
