# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T14:52:20.892235+00:00`
- Correlation status: `ready`
- Asset price records: `463`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `11.29` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.4067` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.1819` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1139` n `12`; crypto_alt avg `-0.0796` n `228`; crypto_major avg `-0.0681` n `8`; equity avg `0.2728` n `65`; fx avg `0.0004` n `4`; index avg `0.1926` n `23`; metal avg `0.0074` n `18`; unknown avg `-0.0287` n `356`
- 1h: commodity avg `-0.1689` n `12`; crypto_alt avg `0.0275` n `228`; crypto_major avg `-0.0585` n `8`; equity avg `0.4919` n `65`; fx avg `0.0026` n `4`; index avg `0.2795` n `23`; metal avg `0.3335` n `18`; unknown avg `3.4837` n `356`
- 4h: commodity avg `1.0442` n `7`; crypto_alt avg `-1.3261` n `223`; crypto_major avg `-1.3625` n `7`; equity avg `-0.7641` n `47`; fx avg `0.1028` n `4`; index avg `-0.1806` n `6`; metal avg `-0.2205` n `7`; unknown avg `8.3016` n `313`
- 24h: commodity avg `-2.558` n `7`; crypto_alt avg `2.3171` n `223`; crypto_major avg `0.9453` n `7`; equity avg `2.0849` n `47`; fx avg `-0.6177` n `4`; index avg `2.1366` n `6`; metal avg `2.6722` n `7`; unknown avg `19.4236` n `311`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.3501`, n `459`, moderate_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.2558`, n `459`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1567`, n `459`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1367`, n `459`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.123`, n `459`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1091`, n `459`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0878`, n `455`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0856`, n `455`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0852`, n `455`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `459`, weak_sample_signal
