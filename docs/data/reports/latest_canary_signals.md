# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T02:37:29.882228+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `13`; crypto_alt avg `0.058` n `237`; crypto_major avg `0.1327` n `8`; equity avg `-0.0055` n `152`; fx avg `-0.0089` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0007` n `20`; unknown avg `0.3784` n `1231`
- 1h: commodity avg `0.0052` n `13`; crypto_alt avg `-0.247` n `237`; crypto_major avg `0.1983` n `8`; equity avg `-0.0179` n `152`; fx avg `-0.014` n `6`; index avg `0.0065` n `26`; metal avg `0.0055` n `20`; unknown avg `162.9571` n `1225`
- 4h: commodity avg `-0.0532` n `13`; crypto_alt avg `-0.0954` n `237`; crypto_major avg `0.6736` n `8`; equity avg `0.1165` n `152`; fx avg `-0.012` n `6`; index avg `0.0133` n `26`; metal avg `0.022` n `20`; unknown avg `0.0619` n `1215`
- 24h: commodity avg `-0.0357` n `13`; crypto_alt avg `-1.3136` n `237`; crypto_major avg `-0.1088` n `8`; equity avg `-0.0709` n `152`; fx avg `-0.0465` n `6`; index avg `-0.0037` n `26`; metal avg `-0.0774` n `20`; unknown avg `0.5599` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
