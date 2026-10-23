# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T02:22:29.875850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0525` n `13`; crypto_alt avg `0.3045` n `237`; crypto_major avg `0.3174` n `8`; equity avg `0.0506` n `151`; fx avg `0.015` n `6`; index avg `0.0057` n `26`; metal avg `0.1044` n `20`; unknown avg `0.2862` n `1233`
- 1h: commodity avg `0.0868` n `13`; crypto_alt avg `0.6295` n `237`; crypto_major avg `0.3458` n `8`; equity avg `0.0143` n `151`; fx avg `0.0476` n `6`; index avg `-0.0504` n `26`; metal avg `0.0044` n `20`; unknown avg `0.0653` n `1231`
- 4h: commodity avg `0.1499` n `13`; crypto_alt avg `0.8615` n `237`; crypto_major avg `0.5739` n `8`; equity avg `0.3424` n `151`; fx avg `-0.0094` n `6`; index avg `-0.0713` n `26`; metal avg `-0.0864` n `20`; unknown avg `0.2775` n `1185`
- 24h: commodity avg `0.5314` n `13`; crypto_alt avg `-2.2641` n `237`; crypto_major avg `-1.3465` n `8`; equity avg `-3.5571` n `151`; fx avg `-0.1465` n `6`; index avg `-0.4739` n `26`; metal avg `-0.7018` n `20`; unknown avg `52.1709` n `905`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1794`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
