# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T12:00:35.595840+00:00`
- Correlation status: `ready`
- Asset price records: `263`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1615` n `7`; crypto_alt avg `0.0767` n `223`; crypto_major avg `0.0416` n `7`; equity avg `0.0781` n `42`; fx avg `-0.0139` n `4`; index avg `-0.0044` n `9`; metal avg `0.0726` n `7`; unknown avg `-0.0348` n `314`
- 1h: commodity avg `-0.2005` n `7`; crypto_alt avg `0.0536` n `223`; crypto_major avg `-0.1111` n `7`; equity avg `0.1893` n `42`; fx avg `-0.0155` n `4`; index avg `0.0458` n `9`; metal avg `-0.2719` n `7`; unknown avg `-0.235` n `314`
- 4h: commodity avg `-0.0302` n `7`; crypto_alt avg `-0.8452` n `223`; crypto_major avg `-1.2023` n `7`; equity avg `-0.6161` n `42`; fx avg `-0.0108` n `4`; index avg `-0.4483` n `9`; metal avg `-0.7972` n `7`; unknown avg `-0.5169` n `314`
- 24h: commodity avg `0.8311` n `7`; crypto_alt avg `0.9714` n `223`; crypto_major avg `0.4612` n `7`; equity avg `0.3279` n `42`; fx avg `-0.0802` n `4`; index avg `0.3972` n `9`; metal avg `-1.7726` n `7`; unknown avg `-0.3177` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2801`, n `259`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2725`, n `259`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.184`, n `259`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1812`, n `255`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1756`, n `255`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1736`, n `255`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1709`, n `259`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1706`, n `255`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.163`, n `259`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1608`, n `255`, weak_sample_signal
