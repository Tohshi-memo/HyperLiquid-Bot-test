# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T21:37:28.464528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `13`; crypto_alt avg `-0.111` n `237`; crypto_major avg `-0.0719` n `8`; equity avg `-0.0032` n `152`; fx avg `-0.0042` n `6`; index avg `0.0055` n `26`; metal avg `0.0029` n `20`; unknown avg `2.2775` n `1230`
- 1h: commodity avg `0.0196` n `13`; crypto_alt avg `0.1476` n `237`; crypto_major avg `0.0963` n `8`; equity avg `-0.021` n `152`; fx avg `0.0254` n `6`; index avg `0.0088` n `26`; metal avg `0.0087` n `20`; unknown avg `0.8414` n `1222`
- 4h: commodity avg `0.0675` n `13`; crypto_alt avg `-0.8888` n `237`; crypto_major avg `-0.4475` n `8`; equity avg `-0.1974` n `152`; fx avg `0.0069` n `6`; index avg `0.0354` n `26`; metal avg `0.0037` n `20`; unknown avg `1.5274` n `1143`
- 24h: commodity avg `0.4613` n `13`; crypto_alt avg `0.2458` n `237`; crypto_major avg `0.3091` n `8`; equity avg `1.3331` n `152`; fx avg `-0.0776` n `6`; index avg `0.137` n `26`; metal avg `-0.1562` n `20`; unknown avg `1.0471` n `1022`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1994`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
