# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T13:07:34.509112+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `13`; crypto_alt avg `-0.1354` n `237`; crypto_major avg `0.0069` n `8`; equity avg `-0.0129` n `152`; fx avg `0.0` n `6`; index avg `-0.0042` n `26`; metal avg `0.0093` n `20`; unknown avg `0.263` n `1228`
- 1h: commodity avg `0.0028` n `13`; crypto_alt avg `0.2127` n `237`; crypto_major avg `0.2787` n `8`; equity avg `0.1284` n `152`; fx avg `-0.0013` n `6`; index avg `0.0229` n `26`; metal avg `0.0183` n `20`; unknown avg `0.0988` n `1230`
- 4h: commodity avg `0.134` n `13`; crypto_alt avg `0.1337` n `237`; crypto_major avg `0.2233` n `8`; equity avg `0.1524` n `152`; fx avg `0.0085` n `6`; index avg `0.0089` n `26`; metal avg `-0.003` n `20`; unknown avg `119.3583` n `1208`
- 24h: commodity avg `0.484` n `13`; crypto_alt avg `-2.5536` n `237`; crypto_major avg `-1.7848` n `8`; equity avg `-0.0794` n `152`; fx avg `0.0127` n `6`; index avg `0.0635` n `26`; metal avg `-0.1704` n `20`; unknown avg `193.8614` n `1053`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1944`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1934`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1904`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1577`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
