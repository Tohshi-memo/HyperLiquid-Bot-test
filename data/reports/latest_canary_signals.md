# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T05:37:28.470719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0277` n `13`; crypto_alt avg `0.1748` n `237`; crypto_major avg `0.1109` n `8`; equity avg `0.1646` n `151`; fx avg `0.0056` n `6`; index avg `0.0161` n `26`; metal avg `0.1002` n `20`; unknown avg `-0.04` n `1231`
- 1h: commodity avg `0.048` n `13`; crypto_alt avg `0.5241` n `237`; crypto_major avg `0.2435` n `8`; equity avg `0.5964` n `151`; fx avg `0.0129` n `6`; index avg `0.0274` n `26`; metal avg `0.1934` n `20`; unknown avg `0.0327` n `1227`
- 4h: commodity avg `0.0439` n `13`; crypto_alt avg `0.9683` n `237`; crypto_major avg `0.5719` n `8`; equity avg `0.5849` n `151`; fx avg `0.0347` n `6`; index avg `0.0295` n `26`; metal avg `0.1719` n `20`; unknown avg `-0.2666` n `1219`
- 24h: commodity avg `0.2987` n `13`; crypto_alt avg `-0.8855` n `237`; crypto_major avg `-0.681` n `8`; equity avg `-1.8858` n `151`; fx avg `-0.113` n `6`; index avg `-0.1621` n `26`; metal avg `-0.405` n `20`; unknown avg `52.9239` n `899`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
