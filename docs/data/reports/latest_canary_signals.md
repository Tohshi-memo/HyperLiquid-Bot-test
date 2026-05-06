# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T10:00:39.414161+00:00`
- Correlation status: `ready`
- Asset price records: `444`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.3395` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.396` n `7`; crypto_alt avg `0.173` n `223`; crypto_major avg `0.1492` n `7`; equity avg `-0.0753` n `47`; fx avg `-0.0082` n `4`; index avg `0.0486` n `6`; metal avg `0.2577` n `7`; unknown avg `0.0816` n `313`
- 1h: commodity avg `-0.5646` n `7`; crypto_alt avg `0.3322` n `223`; crypto_major avg `0.2718` n `7`; equity avg `-0.0407` n `47`; fx avg `-0.0172` n `4`; index avg `-0.0153` n `6`; metal avg `0.2166` n `7`; unknown avg `1.1266` n `313`
- 4h: commodity avg `-1.9629` n `7`; crypto_alt avg `1.8861` n `223`; crypto_major avg `1.3766` n `7`; equity avg `0.6962` n `47`; fx avg `-0.1095` n `4`; index avg `0.6986` n `6`; metal avg `1.1476` n `7`; unknown avg `2.026` n `313`
- 24h: commodity avg `-3.3984` n `7`; crypto_alt avg `4.187` n `223`; crypto_major avg `3.3284` n `7`; equity avg `3.422` n `47`; fx avg `-0.5562` n `4`; index avg `2.8544` n `6`; metal avg `2.8837` n `7`; unknown avg `2.1921` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1706`, n `440`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1645`, n `440`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1471`, n `440`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1343`, n `440`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1217`, n `440`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.118`, n `440`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1105`, n `436`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.097`, n `436`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0957`, n `436`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `436`, weak_sample_signal
