# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T08:30:29.809777+00:00`
- Correlation status: `ready`
- Asset price records: `344`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1399` n `7`; crypto_alt avg `-0.0854` n `223`; crypto_major avg `-0.0701` n `7`; equity avg `0.0409` n `47`; fx avg `0.0101` n `4`; index avg `-0.0042` n `6`; metal avg `-0.041` n `7`; unknown avg `-0.1194` n `312`
- 1h: commodity avg `-0.1878` n `7`; crypto_alt avg `0.0788` n `223`; crypto_major avg `-0.099` n `7`; equity avg `-0.1133` n `47`; fx avg `0.0298` n `4`; index avg `0.2159` n `6`; metal avg `0.0915` n `7`; unknown avg `0.2334` n `312`
- 4h: commodity avg `-0.172` n `7`; crypto_alt avg `0.5157` n `223`; crypto_major avg `0.3459` n `7`; equity avg `0.6762` n `47`; fx avg `0.0187` n `4`; index avg `0.2881` n `6`; metal avg `0.5825` n `7`; unknown avg `0.7151` n `310`
- 24h: commodity avg `0.315` n `7`; crypto_alt avg `1.3197` n `223`; crypto_major avg `0.7086` n `7`; equity avg `0.0756` n `47`; fx avg `0.0088` n `4`; index avg `0.0024` n `6`; metal avg `-0.1307` n `7`; unknown avg `-0.6477` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2185`, n `340`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2115`, n `340`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1386`, n `340`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1342`, n `340`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1183`, n `340`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.108`, n `340`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1056`, n `340`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.105`, n `340`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.103`, n `336`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0969`, n `336`, weak_sample_signal
