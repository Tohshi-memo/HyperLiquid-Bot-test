# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T22:00:29.143613+00:00`
- Correlation status: `ready`
- Asset price records: `396`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `7`; crypto_alt avg `0.1628` n `223`; crypto_major avg `0.4265` n `7`; equity avg `0.0642` n `47`; fx avg `0.0208` n `4`; index avg `-0.01` n `6`; metal avg `-0.0472` n `7`; unknown avg `-0.0901` n `313`
- 1h: commodity avg `0.0477` n `7`; crypto_alt avg `-0.0831` n `223`; crypto_major avg `0.2013` n `7`; equity avg `0.351` n `47`; fx avg `0.1056` n `4`; index avg `0.0343` n `6`; metal avg `0.0376` n `7`; unknown avg `0.9675` n `313`
- 4h: commodity avg `0.0811` n `7`; crypto_alt avg `1.1379` n `223`; crypto_major avg `0.7719` n `7`; equity avg `0.5074` n `47`; fx avg `0.0782` n `4`; index avg `0.1397` n `6`; metal avg `-0.1673` n `7`; unknown avg `1.2426` n `313`
- 24h: commodity avg `-1.161` n `7`; crypto_alt avg `2.0125` n `223`; crypto_major avg `2.3949` n `7`; equity avg `2.2925` n `47`; fx avg `0.0623` n `4`; index avg `1.6129` n `6`; metal avg `0.7109` n `7`; unknown avg `2.3677` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2065`, n `392`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1998`, n `392`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1306`, n `392`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1265`, n `392`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1108`, n `388`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1104`, n `392`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1069`, n `392`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1026`, n `388`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `392`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1001`, n `392`, weak_sample_signal
