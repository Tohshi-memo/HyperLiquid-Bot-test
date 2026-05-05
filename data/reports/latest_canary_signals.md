# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T13:45:31.809776+00:00`
- Correlation status: `ready`
- Asset price records: `365`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1161` n `7`; crypto_alt avg `-0.131` n `223`; crypto_major avg `-0.0193` n `7`; equity avg `0.2963` n `47`; fx avg `-0.0014` n `4`; index avg `0.3617` n `6`; metal avg `-0.1117` n `7`; unknown avg `1.2296` n `312`
- 1h: commodity avg `-0.1928` n `7`; crypto_alt avg `-0.0954` n `223`; crypto_major avg `0.2091` n `7`; equity avg `-0.1085` n `47`; fx avg `0.0033` n `4`; index avg `0.3078` n `6`; metal avg `-0.0994` n `7`; unknown avg `1.2859` n `312`
- 4h: commodity avg `-0.3826` n `7`; crypto_alt avg `0.5313` n `223`; crypto_major avg `1.1678` n `7`; equity avg `0.2907` n `47`; fx avg `0.0385` n `4`; index avg `0.7421` n `6`; metal avg `0.1104` n `7`; unknown avg `1.5761` n `312`
- 24h: commodity avg `-0.0882` n `7`; crypto_alt avg `2.2723` n `223`; crypto_major avg `2.6656` n `7`; equity avg `0.7655` n `47`; fx avg `0.0755` n `4`; index avg `0.8562` n `6`; metal avg `0.3934` n `7`; unknown avg `1.2848` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2088`, n `361`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2016`, n `361`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1338`, n `361`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1298`, n `361`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1091`, n `361`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1054`, n `361`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1042`, n `361`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1037`, n `361`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0914`, n `357`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0895`, n `361`, weak_sample_signal
