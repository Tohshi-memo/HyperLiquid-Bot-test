# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T07:28:44.841474+00:00`
- Correlation status: `ready`
- Asset price records: `244`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0508` n `7`; crypto_alt avg `-0.0219` n `223`; crypto_major avg `0.1453` n `7`; equity avg `0.1565` n `42`; fx avg `-0.0069` n `4`; index avg `0.0203` n `9`; metal avg `-0.1088` n `7`; unknown avg `-0.0108` n `314`
- 1h: commodity avg `0.5581` n `7`; crypto_alt avg `-0.0386` n `223`; crypto_major avg `-0.102` n `7`; equity avg `0.0709` n `42`; fx avg `-0.0024` n `4`; index avg `-0.025` n `9`; metal avg `-0.3256` n `7`; unknown avg `-0.1179` n `314`
- 4h: commodity avg `0.3373` n `7`; crypto_alt avg `-0.057` n `223`; crypto_major avg `-0.4068` n `7`; equity avg `-0.3398` n `42`; fx avg `-0.0525` n `4`; index avg `0.0479` n `9`; metal avg `-0.8005` n `7`; unknown avg `-0.4304` n `312`
- 24h: commodity avg `0.4911` n `7`; crypto_alt avg `2.1855` n `223`; crypto_major avg `2.2588` n `7`; equity avg `1.1827` n `42`; fx avg `-0.0329` n `4`; index avg `0.9046` n `9`; metal avg `-0.4378` n `7`; unknown avg `-0.1715` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3915`, n `236`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3828`, n `236`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.354`, n `240`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3409`, n `240`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2091`, n `236`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1986`, n `236`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1783`, n `240`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1723`, n `240`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1687`, n `236`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.158`, n `240`, weak_sample_signal
