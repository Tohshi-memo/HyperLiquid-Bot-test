# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T22:45:43.671263+00:00`
- Correlation status: `ready`
- Asset price records: `399`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0302` n `7`; crypto_alt avg `-0.5043` n `223`; crypto_major avg `-0.5166` n `7`; equity avg `0.0565` n `47`; fx avg `0.0024` n `4`; index avg `0.0003` n `6`; metal avg `0.0503` n `7`; unknown avg `1.091` n `313`
- 1h: commodity avg `-0.0763` n `7`; crypto_alt avg `-0.354` n `223`; crypto_major avg `-0.076` n `7`; equity avg `0.2456` n `47`; fx avg `0.0314` n `4`; index avg `0.016` n `6`; metal avg `-0.2185` n `7`; unknown avg `0.0385` n `313`
- 4h: commodity avg `-0.0196` n `7`; crypto_alt avg `0.4258` n `223`; crypto_major avg `0.1297` n `7`; equity avg `0.6905` n `47`; fx avg `0.1182` n `4`; index avg `0.1368` n `6`; metal avg `-0.3386` n `7`; unknown avg `1.3705` n `313`
- 24h: commodity avg `-1.1659` n `7`; crypto_alt avg `1.9165` n `223`; crypto_major avg `2.276` n `7`; equity avg `2.6299` n `47`; fx avg `0.0737` n `4`; index avg `1.7123` n `6`; metal avg `0.5719` n `7`; unknown avg `2.4726` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2064`, n `395`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1997`, n `395`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1303`, n `395`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1262`, n `395`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1118`, n `395`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1109`, n `391`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1061`, n `395`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1026`, n `391`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `395`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `395`, weak_sample_signal
