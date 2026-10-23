# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T05:07:29.176004+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `13`; crypto_alt avg `0.138` n `237`; crypto_major avg `0.1145` n `8`; equity avg `0.3617` n `151`; fx avg `0.0108` n `6`; index avg `0.0274` n `26`; metal avg `0.0663` n `20`; unknown avg `0.1417` n `1229`
- 1h: commodity avg `0.0188` n `13`; crypto_alt avg `-0.0222` n `237`; crypto_major avg `-0.039` n `8`; equity avg `0.0877` n `151`; fx avg `0.0124` n `6`; index avg `-0.0112` n `26`; metal avg `0.0166` n `20`; unknown avg `0.1294` n `1229`
- 4h: commodity avg `0.0282` n `13`; crypto_alt avg `1.1645` n `237`; crypto_major avg `0.6412` n `8`; equity avg `0.7431` n `151`; fx avg `0.0773` n `6`; index avg `0.0523` n `26`; metal avg `0.0035` n `20`; unknown avg `-0.1802` n `1221`
- 24h: commodity avg `0.2912` n `13`; crypto_alt avg `-1.4725` n `237`; crypto_major avg `-0.9921` n `8`; equity avg `-2.3624` n `151`; fx avg `-0.1142` n `6`; index avg `-0.2244` n `26`; metal avg `-0.5579` n `20`; unknown avg `52.9048` n `901`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1709`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
