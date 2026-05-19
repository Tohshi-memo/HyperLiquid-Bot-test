# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T05:07:15.886635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0538` n `12`; crypto_alt avg `-0.0255` n `228`; crypto_major avg `-0.1261` n `8`; equity avg `-0.0187` n `66`; fx avg `0.0022` n `6`; index avg `0.0479` n `23`; metal avg `0.0277` n `18`; unknown avg `0.2406` n `383`
- 1h: commodity avg `-0.0928` n `12`; crypto_alt avg `0.1325` n `228`; crypto_major avg `-0.0301` n `8`; equity avg `-0.0228` n `66`; fx avg `0.0056` n `6`; index avg `0.0555` n `23`; metal avg `0.1246` n `18`; unknown avg `0.3147` n `383`
- 4h: commodity avg `-0.0728` n `12`; crypto_alt avg `-0.0244` n `228`; crypto_major avg `-0.3724` n `8`; equity avg `-0.3756` n `66`; fx avg `0.0501` n `6`; index avg `-0.2507` n `23`; metal avg `-0.8845` n `18`; unknown avg `-0.3612` n `383`
- 24h: commodity avg `0.0915` n `12`; crypto_alt avg `0.846` n `228`; crypto_major avg `0.1432` n `8`; equity avg `-1.0079` n `66`; fx avg `0.2557` n `6`; index avg `-0.4442` n `23`; metal avg `0.4781` n `18`; unknown avg `0.6806` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
