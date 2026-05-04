# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T20:45:27.500710+00:00`
- Correlation status: `ready`
- Asset price records: `297`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `7`; crypto_alt avg `-0.1659` n `223`; crypto_major avg `-0.0636` n `7`; equity avg `0.0277` n `47`; fx avg `-0.0016` n `4`; index avg `0.0215` n `6`; metal avg `0.0135` n `7`; unknown avg `0.0154` n `312`
- 1h: commodity avg `-0.1075` n `7`; crypto_alt avg `-0.2526` n `223`; crypto_major avg `-0.1274` n `7`; equity avg `-0.2135` n `47`; fx avg `0.0151` n `4`; index avg `0.1469` n `6`; metal avg `-0.076` n `7`; unknown avg `0.0152` n `312`
- 4h: commodity avg `-0.4367` n `7`; crypto_alt avg `-0.1179` n `223`; crypto_major avg `-0.3776` n `7`; equity avg `-0.4023` n `47`; fx avg `0.0179` n `4`; index avg `0.0674` n `6`; metal avg `0.1129` n `7`; unknown avg `-0.2302` n `312`
- 24h: commodity avg `1.8259` n `7`; crypto_alt avg `1.1335` n `223`; crypto_major avg `0.4904` n `7`; equity avg `-0.42` n `47`; fx avg `-0.062` n `4`; index avg `-0.0961` n `6`; metal avg `-2.3993` n `7`; unknown avg `-1.0906` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2367`, n `293`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2309`, n `293`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1888`, n `289`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.187`, n `289`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1501`, n `293`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1494`, n `293`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1439`, n `293`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1297`, n `293`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `289`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1208`, n `293`, weak_sample_signal
