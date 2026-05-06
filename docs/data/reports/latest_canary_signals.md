# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T14:07:27.067613+00:00`
- Correlation status: `ready`
- Asset price records: `460`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `22.18` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.5093` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.706` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.6783` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_metal_divergence: score `-1.6302` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.4793` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2733` n `12`; crypto_alt avg `-0.7266` n `228`; crypto_major avg `-0.5394` n `8`; equity avg `-0.273` n `65`; fx avg `0.0275` n `4`; index avg `-0.0376` n `23`; metal avg `0.0695` n `18`; unknown avg `0.8396` n `356`
- 1h: commodity avg `-0.0518` n `7`; crypto_alt avg `-1.4479` n `223`; crypto_major avg `-1.4402` n `7`; equity avg `-0.6449` n `47`; fx avg `-0.0302` n `4`; index avg `0.0391` n `6`; metal avg `0.2381` n `7`; unknown avg `0.2119` n `313`
- 4h: commodity avg `0.6607` n `7`; crypto_alt avg `-2.0311` n `223`; crypto_major avg `-1.8486` n `7`; equity avg `-1.1655` n `47`; fx avg `0.0264` n `4`; index avg `-0.1426` n `6`; metal avg `-0.2184` n `7`; unknown avg `0.2191` n `313`
- 24h: commodity avg `-2.2382` n `7`; crypto_alt avg `1.5041` n `223`; crypto_major avg `0.496` n `7`; equity avg `2.1421` n `47`; fx avg `-0.5813` n `4`; index avg `2.214` n `6`; metal avg `2.3325` n `7`; unknown avg `3.9129` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1644`, n `456`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1585`, n `456`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1402`, n `456`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1249`, n `456`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `456`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1103`, n `456`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0952`, n `452`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.087`, n `452`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0862`, n `452`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0861`, n `456`, weak_sample_signal
