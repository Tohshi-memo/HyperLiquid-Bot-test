# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T01:52:11.264855+00:00`
- Correlation status: `ready`
- Asset price records: `507`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.66` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.6061` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.1709` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0953` n `12`; crypto_alt avg `-0.1122` n `228`; crypto_major avg `-0.1189` n `8`; equity avg `0.2141` n `65`; fx avg `-0.017` n `4`; index avg `0.0863` n `23`; metal avg `0.3` n `18`; unknown avg `-0.0864` n `358`
- 1h: commodity avg `-0.3351` n `12`; crypto_alt avg `-0.3051` n `228`; crypto_major avg `-0.2079` n `8`; equity avg `0.2294` n `65`; fx avg `-0.0309` n `4`; index avg `0.1077` n `23`; metal avg `0.6773` n `18`; unknown avg `0.7731` n `357`
- 4h: commodity avg `-0.2974` n `12`; crypto_alt avg `-1.3791` n `228`; crypto_major avg `-0.9984` n `8`; equity avg `0.3299` n `65`; fx avg `0.0457` n `4`; index avg `0.1725` n `23`; metal avg `0.6077` n `18`; unknown avg `0.6814` n `356`
- 24h: commodity avg `-1.7271` n `7`; crypto_alt avg `0.5299` n `223`; crypto_major avg `-0.667` n `7`; equity avg `1.6507` n `47`; fx avg `-0.2676` n `4`; index avg `1.1038` n `6`; metal avg `2.5929` n `7`; unknown avg `4.1781` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1399`, n `503`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1236`, n `503`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `503`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0732`, n `499`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0675`, n `503`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0673`, n `503`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0664`, n `499`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0643`, n `499`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0634`, n `499`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0552`, n `499`, weak_sample_signal
