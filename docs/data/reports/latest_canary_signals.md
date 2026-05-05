# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T22:10:46.357943+00:00`
- Correlation status: `ready`
- Asset price records: `396`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0263` n `7`; crypto_alt avg `0.1122` n `223`; crypto_major avg `0.375` n `7`; equity avg `0.0453` n `47`; fx avg `0.0283` n `4`; index avg `0.005` n `6`; metal avg `-0.1493` n `7`; unknown avg `-0.1367` n `313`
- 1h: commodity avg `0.0112` n `7`; crypto_alt avg `-0.134` n `223`; crypto_major avg `0.1501` n `7`; equity avg `0.333` n `47`; fx avg `0.1131` n `4`; index avg `0.0493` n `6`; metal avg `-0.0645` n `7`; unknown avg `0.9363` n `313`
- 4h: commodity avg `0.0445` n `7`; crypto_alt avg `1.0854` n `223`; crypto_major avg `0.7199` n `7`; equity avg `0.4899` n `47`; fx avg `0.0856` n `4`; index avg `0.1547` n `6`; metal avg `-0.2691` n `7`; unknown avg `1.1893` n `313`
- 24h: commodity avg `-1.1964` n `7`; crypto_alt avg `1.9604` n `223`; crypto_major avg `2.3437` n `7`; equity avg `2.2798` n `47`; fx avg `0.0698` n `4`; index avg `1.6282` n `6`; metal avg `0.6082` n `7`; unknown avg `2.3002` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2066`, n `392`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1998`, n `392`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1306`, n `392`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1265`, n `392`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1107`, n `392`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1107`, n `388`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.107`, n `392`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1025`, n `388`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `392`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1001`, n `392`, weak_sample_signal
