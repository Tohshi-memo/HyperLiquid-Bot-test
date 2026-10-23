# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T10:22:37.846004+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0231` n `13`; crypto_alt avg `0.2048` n `237`; crypto_major avg `0.156` n `8`; equity avg `0.0932` n `152`; fx avg `0.0048` n `6`; index avg `0.0151` n `26`; metal avg `0.0249` n `20`; unknown avg `-0.1576` n `1233`
- 1h: commodity avg `0.0332` n `13`; crypto_alt avg `-0.0239` n `237`; crypto_major avg `-0.0256` n `8`; equity avg `-0.2858` n `152`; fx avg `0.0131` n `6`; index avg `-0.0399` n `26`; metal avg `-0.0522` n `20`; unknown avg `0.0415` n `1231`
- 4h: commodity avg `0.0645` n `13`; crypto_alt avg `-0.1608` n `237`; crypto_major avg `-0.038` n `8`; equity avg `-0.3041` n `152`; fx avg `-0.0654` n `6`; index avg `-0.1109` n `26`; metal avg `-0.0965` n `20`; unknown avg `-0.1718` n `1151`
- 24h: commodity avg `0.306` n `13`; crypto_alt avg `-0.0811` n `237`; crypto_major avg `0.1676` n `8`; equity avg `-1.1445` n `152`; fx avg `-0.0429` n `6`; index avg `-0.1474` n `26`; metal avg `-0.4757` n `20`; unknown avg `49.6528` n `950`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2061`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1865`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
