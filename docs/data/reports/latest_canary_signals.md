# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T20:00:33.974744+00:00`
- Correlation status: `ready`
- Asset price records: `388`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0324` n `7`; crypto_alt avg `0.0814` n `223`; crypto_major avg `0.0746` n `7`; equity avg `-0.0904` n `47`; fx avg `0.0141` n `4`; index avg `-0.0085` n `6`; metal avg `-0.0456` n `7`; unknown avg `-0.0296` n `313`
- 1h: commodity avg `0.0175` n `7`; crypto_alt avg `0.252` n `223`; crypto_major avg `0.1481` n `7`; equity avg `-0.1396` n `47`; fx avg `0.0182` n `4`; index avg `-0.0375` n `6`; metal avg `-0.1939` n `7`; unknown avg `0.0623` n `313`
- 4h: commodity avg `0.017` n `7`; crypto_alt avg `0.463` n `223`; crypto_major avg `0.3054` n `7`; equity avg `0.0122` n `47`; fx avg `0.0085` n `4`; index avg `0.1185` n `6`; metal avg `-0.4337` n `7`; unknown avg `-0.0501` n `313`
- 24h: commodity avg `-1.1946` n `7`; crypto_alt avg `1.9373` n `223`; crypto_major avg `2.4537` n `7`; equity avg `1.9097` n `47`; fx avg `-0.0216` n `4`; index avg `1.2981` n `6`; metal avg `0.6216` n `7`; unknown avg `2.1272` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2068`, n `384`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2`, n `384`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1315`, n `384`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1274`, n `384`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1138`, n `380`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1113`, n `384`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1072`, n `384`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.106`, n `380`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `384`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1035`, n `384`, weak_sample_signal
