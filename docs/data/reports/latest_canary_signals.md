# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T13:52:19.829080+00:00`
- Correlation status: `ready`
- Asset price records: `459`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `90.06` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.664` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.6469` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.0192` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1672` n `12`; crypto_alt avg `-0.324` n `228`; crypto_major avg `-0.3433` n `8`; equity avg `0.0185` n `65`; fx avg `-0.0076` n `4`; index avg `-0.0452` n `23`; metal avg `-0.0371` n `18`; unknown avg `-0.2546` n `356`
- 1h: commodity avg `0.0171` n `7`; crypto_alt avg `-1.385` n `223`; crypto_major avg `-1.6532` n `7`; equity avg `-0.5228` n `47`; fx avg `-0.017` n `4`; index avg `0.0108` n `6`; metal avg `-0.0063` n `7`; unknown avg `0.1244` n `313`
- 4h: commodity avg `0.1046` n `7`; crypto_alt avg `-1.14` n `223`; crypto_major avg `-1.0933` n `7`; equity avg `-0.9246` n `47`; fx avg `-0.0094` n `4`; index avg `-0.0741` n `6`; metal avg `-0.0234` n `7`; unknown avg `-0.0805` n `313`
- 24h: commodity avg `-2.5678` n `7`; crypto_alt avg `2.2878` n `223`; crypto_major avg `0.9144` n `7`; equity avg `2.0622` n `47`; fx avg `-0.606` n `4`; index avg `1.9722` n `6`; metal avg `2.4623` n `7`; unknown avg `1.8537` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1647`, n `455`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1588`, n `455`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1412`, n `455`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1252`, n `455`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1151`, n `455`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1118`, n `455`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0952`, n `451`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0872`, n `455`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0871`, n `451`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0868`, n `455`, weak_sample_signal
