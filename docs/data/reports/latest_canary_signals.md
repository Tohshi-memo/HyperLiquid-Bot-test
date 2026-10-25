# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T01:22:35.814938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `13`; crypto_alt avg `-0.0995` n `237`; crypto_major avg `-0.0261` n `8`; equity avg `-0.0024` n `152`; fx avg `-0.0044` n `6`; index avg `-0.0075` n `26`; metal avg `-0.0024` n `20`; unknown avg `0.1011` n `1227`
- 1h: commodity avg `0.0092` n `13`; crypto_alt avg `-0.2051` n `237`; crypto_major avg `0.0672` n `8`; equity avg `0.0533` n `152`; fx avg `0.0049` n `6`; index avg `0.0036` n `26`; metal avg `0.0013` n `20`; unknown avg `1.1551` n `1225`
- 4h: commodity avg `-0.0419` n `13`; crypto_alt avg `0.5897` n `237`; crypto_major avg `0.6993` n `8`; equity avg `0.2805` n `152`; fx avg `-0.0039` n `6`; index avg `0.0237` n `26`; metal avg `0.0319` n `20`; unknown avg `-0.0676` n `1151`
- 24h: commodity avg `-0.0664` n `13`; crypto_alt avg `-1.0394` n `237`; crypto_major avg `-0.2135` n `8`; equity avg `0.0835` n `152`; fx avg `-0.037` n `6`; index avg `0.0072` n `26`; metal avg `-0.0732` n `20`; unknown avg `1.2808` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
