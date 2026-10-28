# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T04:37:30.758819+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.6` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0267` n `13`; crypto_alt avg `0.1713` n `238`; crypto_major avg `0.1319` n `8`; equity avg `-0.129` n `154`; fx avg `0.0058` n `6`; index avg `-0.0259` n `27`; metal avg `-0.0037` n `20`; unknown avg `0.5763` n `1238`
- 1h: commodity avg `0.0413` n `13`; crypto_alt avg `-0.2223` n `238`; crypto_major avg `-0.2131` n `8`; equity avg `-0.2363` n `154`; fx avg `0.0118` n `6`; index avg `-0.0572` n `27`; metal avg `-0.0403` n `20`; unknown avg `0.358` n `1224`
- 4h: commodity avg `0.128` n `13`; crypto_alt avg `0.3676` n `238`; crypto_major avg `0.4512` n `8`; equity avg `0.9148` n `154`; fx avg `0.1` n `6`; index avg `0.0915` n `27`; metal avg `-0.1507` n `20`; unknown avg `-0.2511` n `1214`
- 24h: commodity avg `0.0558` n `13`; crypto_alt avg `2.2224` n `237`; crypto_major avg `2.1799` n `8`; equity avg `3.1586` n `154`; fx avg `0.1048` n `6`; index avg `0.4902` n `27`; metal avg `0.1362` n `20`; unknown avg `15.575` n `1016`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1708`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1684`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
