# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T00:07:35.824336+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0457` n `13`; crypto_alt avg `-0.0358` n `237`; crypto_major avg `-0.0198` n `8`; equity avg `-0.0642` n `151`; fx avg `-0.0325` n `6`; index avg `-0.064` n `26`; metal avg `-0.003` n `20`; unknown avg `0.0044` n `1225`
- 1h: commodity avg `0.0047` n `13`; crypto_alt avg `0.024` n `237`; crypto_major avg `0.0039` n `8`; equity avg `-0.4186` n `151`; fx avg `-0.0359` n `6`; index avg `-0.1143` n `26`; metal avg `-0.0432` n `20`; unknown avg `0.087` n `1225`
- 4h: commodity avg `-0.0072` n `13`; crypto_alt avg `-0.2012` n `237`; crypto_major avg `-0.0373` n `8`; equity avg `-0.8214` n `151`; fx avg `-0.0497` n `6`; index avg `-0.1531` n `26`; metal avg `-0.0418` n `20`; unknown avg `0.067` n `1135`
- 24h: commodity avg `0.4721` n `13`; crypto_alt avg `-4.8845` n `237`; crypto_major avg `-3.472` n `8`; equity avg `-5.3381` n `151`; fx avg `-0.1986` n `6`; index avg `-0.642` n `26`; metal avg `-1.0061` n `20`; unknown avg `54.6227` n `905`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1827`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1667`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
