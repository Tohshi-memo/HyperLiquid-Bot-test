# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T06:30:24.639365+00:00`
- Correlation status: `ready`
- Asset price records: `241`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1199` n `7`; crypto_alt avg `-0.2754` n `223`; crypto_major avg `-0.4105` n `7`; equity avg `-0.0325` n `42`; fx avg `-0.0005` n `4`; index avg `0.0117` n `9`; metal avg `0.0489` n `7`; unknown avg `-0.1142` n `314`
- 1h: commodity avg `0.0788` n `7`; crypto_alt avg `-0.2407` n `223`; crypto_major avg `-0.7096` n `7`; equity avg `-0.1116` n `42`; fx avg `0.0152` n `4`; index avg `0.0202` n `9`; metal avg `-0.0642` n `7`; unknown avg `-0.2102` n `312`
- 4h: commodity avg `-0.145` n `7`; crypto_alt avg `0.1183` n `223`; crypto_major avg `-0.132` n `7`; equity avg `-0.0572` n `42`; fx avg `-0.0346` n `4`; index avg `0.3978` n `9`; metal avg `-0.0065` n `7`; unknown avg `-0.2401` n `312`
- 24h: commodity avg `0.0613` n `7`; crypto_alt avg `2.2399` n `223`; crypto_major avg `2.1902` n `7`; equity avg `1.034` n `42`; fx avg `-0.0272` n `4`; index avg `0.9348` n `9`; metal avg `-0.0521` n `7`; unknown avg `0.075` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.407`, n `233`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3974`, n `233`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3607`, n `237`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3465`, n `237`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2005`, n `233`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1922`, n `233`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1789`, n `237`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1785`, n `237`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1728`, n `237`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1577`, n `233`, weak_sample_signal
