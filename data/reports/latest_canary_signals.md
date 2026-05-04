# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T20:00:29.416809+00:00`
- Correlation status: `ready`
- Asset price records: `294`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `7`; crypto_alt avg `-0.0074` n `223`; crypto_major avg `-0.0043` n `7`; equity avg `-0.133` n `46`; fx avg `-0.0014` n `4`; index avg `0.1818` n `6`; metal avg `-0.0498` n `7`; unknown avg `0.0191` n `313`
- 1h: commodity avg `-0.1398` n `7`; crypto_alt avg `-0.3769` n `223`; crypto_major avg `-0.2785` n `7`; equity avg `-0.2565` n `46`; fx avg `0.0114` n `4`; index avg `0.1395` n `6`; metal avg `0.0142` n `7`; unknown avg `-0.1663` n `313`
- 4h: commodity avg `-0.0248` n `7`; crypto_alt avg `0.4431` n `223`; crypto_major avg `0.1811` n `7`; equity avg `-0.5963` n `46`; fx avg `-0.0266` n `4`; index avg `-0.0701` n `6`; metal avg `-0.1245` n `7`; unknown avg `-0.0259` n `313`
- 24h: commodity avg `1.5941` n `7`; crypto_alt avg `1.5875` n `223`; crypto_major avg `0.7838` n `7`; equity avg `-0.3979` n `46`; fx avg `-0.0782` n `4`; index avg `0.0023` n `6`; metal avg `-2.4127` n `7`; unknown avg `-1.0428` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2364`, n `290`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2305`, n `290`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1608`, n `286`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1595`, n `286`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1504`, n `290`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1489`, n `290`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1435`, n `290`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1293`, n `290`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1222`, n `286`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1204`, n `290`, weak_sample_signal
