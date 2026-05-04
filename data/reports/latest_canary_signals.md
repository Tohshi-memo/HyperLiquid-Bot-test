# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T18:45:21.658747+00:00`
- Correlation status: `ready`
- Asset price records: `289`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0786` n `7`; crypto_alt avg `0.0328` n `223`; crypto_major avg `-0.1745` n `7`; equity avg `-0.248` n `42`; fx avg `-0.0075` n `4`; index avg `-0.005` n `9`; metal avg `0.0001` n `7`; unknown avg `0.0082` n `314`
- 1h: commodity avg `0.1561` n `7`; crypto_alt avg `-0.1367` n `223`; crypto_major avg `-0.4694` n `7`; equity avg `-0.2538` n `42`; fx avg `-0.0045` n `4`; index avg `-0.0474` n `9`; metal avg `-0.2217` n `7`; unknown avg `0.003` n `314`
- 4h: commodity avg `0.8795` n `7`; crypto_alt avg `0.6016` n `223`; crypto_major avg `0.0045` n `7`; equity avg `-1.3862` n `42`; fx avg `-0.014` n `4`; index avg `-0.569` n `9`; metal avg `-1.2327` n `7`; unknown avg `-0.275` n `314`
- 24h: commodity avg `1.8232` n `7`; crypto_alt avg `2.0188` n `223`; crypto_major avg `1.1966` n `7`; equity avg `-0.3504` n `42`; fx avg `-0.0459` n `4`; index avg `0.4629` n `9`; metal avg `-2.5079` n `7`; unknown avg `-0.8328` n `312`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2377`, n `285`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.232`, n `285`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1637`, n `281`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1627`, n `281`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.15`, n `285`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1476`, n `285`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1427`, n `285`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1322`, n `281`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1321`, n `281`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1289`, n `281`, weak_sample_signal
