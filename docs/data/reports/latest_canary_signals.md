# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T09:00:32.753107+00:00`
- Correlation status: `ready`
- Asset price records: `251`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0105` n `7`; crypto_alt avg `0.0793` n `223`; crypto_major avg `-0.0557` n `7`; equity avg `-0.0215` n `42`; fx avg `0.0011` n `4`; index avg `-0.028` n `9`; metal avg `-0.065` n `7`; unknown avg `-0.0181` n `314`
- 1h: commodity avg `-0.2013` n `7`; crypto_alt avg `-0.0199` n `223`; crypto_major avg `-0.134` n `7`; equity avg `-0.1654` n `42`; fx avg `0.0141` n `4`; index avg `-0.153` n `9`; metal avg `-0.0928` n `7`; unknown avg `-0.1627` n `314`
- 4h: commodity avg `0.4105` n `7`; crypto_alt avg `-0.4701` n `223`; crypto_major avg `-1.0777` n `7`; equity avg `-0.3301` n `42`; fx avg `0.0186` n `4`; index avg `-0.1064` n `9`; metal avg `-1.1247` n `7`; unknown avg `-0.1587` n `312`
- 24h: commodity avg `0.5775` n `7`; crypto_alt avg `1.9305` n `223`; crypto_major avg `1.8897` n `7`; equity avg `1.006` n `42`; fx avg `-0.0499` n `4`; index avg `0.7414` n `9`; metal avg `-1.0115` n `7`; unknown avg `0.1124` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3359`, n `247`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3251`, n `247`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.2989`, n `243`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2942`, n `243`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2217`, n `243`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.2084`, n `243`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1973`, n `247`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1852`, n `243`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1783`, n `247`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1721`, n `247`, weak_sample_signal
