# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T13:37:27.419077+00:00`
- Correlation status: `ready`
- Asset price records: `458`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `24.29` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.0455` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.4246` n `12`; crypto_alt avg `-0.3037` n `228`; crypto_major avg `-0.3434` n `8`; equity avg `-0.2154` n `65`; fx avg `-0.0366` n `4`; index avg `0.1184` n `23`; metal avg `0.3129` n `18`; unknown avg `0.3638` n `356`
- 1h: commodity avg `-0.0432` n `7`; crypto_alt avg `-0.8971` n `223`; crypto_major avg `-1.2644` n `7`; equity avg `-0.5869` n `47`; fx avg `0.0161` n `4`; index avg `-0.2189` n `6`; metal avg `0.0654` n `7`; unknown avg `1.0542` n `313`
- 4h: commodity avg `0.2158` n `7`; crypto_alt avg `-0.6974` n `223`; crypto_major avg `-0.6889` n `7`; equity avg `-0.8755` n `47`; fx avg `0.0022` n `4`; index avg `-0.108` n `6`; metal avg `-0.017` n `7`; unknown avg `0.9584` n `313`
- 24h: commodity avg `-2.7975` n `7`; crypto_alt avg `2.5062` n `223`; crypto_major avg `1.291` n `7`; equity avg `2.4456` n `47`; fx avg `-0.6001` n `4`; index avg `2.3585` n `6`; metal avg `2.399` n `7`; unknown avg `3.7457` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1647`, n `454`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1587`, n `454`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1412`, n `454`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1251`, n `454`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1174`, n `454`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.114`, n `454`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0952`, n `450`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0884`, n `454`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0879`, n `454`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0871`, n `450`, weak_sample_signal
