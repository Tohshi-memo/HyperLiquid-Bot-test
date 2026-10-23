# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T19:22:39.392498+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `13`; crypto_alt avg `-0.4065` n `237`; crypto_major avg `-0.3099` n `8`; equity avg `0.0557` n `152`; fx avg `-0.002` n `6`; index avg `0.0129` n `26`; metal avg `-0.0028` n `20`; unknown avg `1.0397` n `1230`
- 1h: commodity avg `0.0259` n `13`; crypto_alt avg `-1.0796` n `237`; crypto_major avg `-0.6499` n `8`; equity avg `-0.2244` n `152`; fx avg `0.0007` n `6`; index avg `-0.0227` n `26`; metal avg `-0.0274` n `20`; unknown avg `73.5907` n `1230`
- 4h: commodity avg `0.235` n `13`; crypto_alt avg `-0.6825` n `237`; crypto_major avg `-0.7112` n `8`; equity avg `-0.2597` n `152`; fx avg `-0.0019` n `6`; index avg `-0.0403` n `26`; metal avg `-0.0918` n `20`; unknown avg `-0.3613` n `1197`
- 24h: commodity avg `0.338` n `13`; crypto_alt avg `0.1532` n `237`; crypto_major avg `-0.0313` n `8`; equity avg `1.2237` n `152`; fx avg `-0.0912` n `6`; index avg `0.0532` n `26`; metal avg `-0.1425` n `20`; unknown avg `-0.7148` n `1036`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2013`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1789`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
