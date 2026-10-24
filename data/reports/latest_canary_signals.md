# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T21:16:18.813625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `13`; crypto_alt avg `-0.0827` n `237`; crypto_major avg `-0.0072` n `8`; equity avg `-0.0414` n `152`; fx avg `-0.0219` n `6`; index avg `-0.0103` n `26`; metal avg `-0.0095` n `20`; unknown avg `-0.0456` n `1231`
- 1h: commodity avg `-0.0372` n `13`; crypto_alt avg `-0.2719` n `237`; crypto_major avg `-0.2026` n `8`; equity avg `-0.1319` n `152`; fx avg `-0.014` n `6`; index avg `-0.0158` n `26`; metal avg `-0.0231` n `20`; unknown avg `0.4889` n `1223`
- 4h: commodity avg `-0.0197` n `13`; crypto_alt avg `0.5818` n `237`; crypto_major avg `0.6482` n `8`; equity avg `0.1702` n `152`; fx avg `-0.0185` n `6`; index avg `0.024` n `26`; metal avg `0.0135` n `20`; unknown avg `0.4987` n `1175`
- 24h: commodity avg `0.0669` n `13`; crypto_alt avg `-2.5051` n `237`; crypto_major avg `-1.7776` n `8`; equity avg `-0.3533` n `152`; fx avg `-0.0529` n `6`; index avg `-0.0645` n `26`; metal avg `-0.1672` n `20`; unknown avg `0.6517` n `1076`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1803`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
