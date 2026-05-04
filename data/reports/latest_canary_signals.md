# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T15:45:51.580998+00:00`
- Correlation status: `ready`
- Asset price records: `278`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1372` n `7`; crypto_alt avg `-0.0639` n `223`; crypto_major avg `-0.0096` n `7`; equity avg `-0.2348` n `42`; fx avg `0.0109` n `4`; index avg `-0.0707` n `9`; metal avg `-0.0545` n `7`; unknown avg `-0.015` n `314`
- 1h: commodity avg `0.6941` n `7`; crypto_alt avg `-0.1749` n `223`; crypto_major avg `-0.395` n `7`; equity avg `-0.965` n `42`; fx avg `0.0044` n `4`; index avg `-0.353` n `9`; metal avg `-1.0096` n `7`; unknown avg `-0.3742` n `314`
- 4h: commodity avg `0.5663` n `7`; crypto_alt avg `0.517` n `223`; crypto_major avg `0.413` n `7`; equity avg `0.0712` n `42`; fx avg `0.0091` n `4`; index avg `0.3272` n `9`; metal avg `-0.1621` n `7`; unknown avg `-0.5065` n `314`
- 24h: commodity avg `1.8816` n `7`; crypto_alt avg `1.4544` n `223`; crypto_major avg `0.8398` n `7`; equity avg `0.3029` n `42`; fx avg `-0.0719` n `4`; index avg `0.724` n `9`; metal avg `-2.082` n `7`; unknown avg `-0.4882` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2453`, n `274`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2386`, n `274`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.217`, n `270`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.2151`, n `270`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1518`, n `274`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1516`, n `274`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1463`, n `274`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1343`, n `270`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.133`, n `270`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1323`, n `274`, weak_sample_signal
