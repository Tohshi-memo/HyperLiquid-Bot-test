# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T08:15:32.965859+00:00`
- Correlation status: `ready`
- Asset price records: `437`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1205` n `7`; crypto_alt avg `0.2271` n `223`; crypto_major avg `0.1836` n `7`; equity avg `0.0676` n `47`; fx avg `0.0415` n `4`; index avg `0.0422` n `6`; metal avg `-0.0372` n `7`; unknown avg `0.1302` n `313`
- 1h: commodity avg `-0.5929` n `7`; crypto_alt avg `0.3868` n `223`; crypto_major avg `0.2492` n `7`; equity avg `0.1537` n `47`; fx avg `-0.1085` n `4`; index avg `-0.0428` n `6`; metal avg `0.4379` n `7`; unknown avg `0.3319` n `313`
- 4h: commodity avg `-0.5309` n `7`; crypto_alt avg `0.7387` n `223`; crypto_major avg `0.3956` n `7`; equity avg `0.296` n `47`; fx avg `-0.2658` n `4`; index avg `-0.035` n `6`; metal avg `0.3885` n `7`; unknown avg `1.1495` n `311`
- 24h: commodity avg `-1.913` n `7`; crypto_alt avg `2.8871` n `223`; crypto_major avg `2.0449` n `7`; equity avg `2.753` n `47`; fx avg `-0.4594` n `4`; index avg `1.8753` n `6`; metal avg `2.1129` n `7`; unknown avg `1.9161` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1785`, n `433`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1723`, n `433`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1317`, n `433`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1247`, n `433`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1209`, n `433`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1154`, n `433`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.097`, n `429`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0942`, n `429`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0928`, n `433`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0922`, n `433`, weak_sample_signal
