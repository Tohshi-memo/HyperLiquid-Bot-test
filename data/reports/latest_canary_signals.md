# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T10:52:31.558363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1114` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.6442` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5429` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0648` n `13`; crypto_alt avg `-0.3451` n `239`; crypto_major avg `-0.4462` n `8`; equity avg `-0.5525` n `166`; fx avg `-0.0045` n `6`; index avg `-0.0792` n `27`; metal avg `-0.0658` n `20`; unknown avg `157.7968` n `1266`
- 1h: commodity avg `-0.0124` n `13`; crypto_alt avg `-0.6067` n `239`; crypto_major avg `-0.7971` n `8`; equity avg `-1.0595` n `166`; fx avg `0.0109` n `6`; index avg `-0.1578` n `27`; metal avg `-0.0904` n `20`; unknown avg `327.4876` n `1220`
- 4h: commodity avg `0.1923` n `13`; crypto_alt avg `-2.2769` n `239`; crypto_major avg `-1.9191` n `8`; equity avg `-2.9558` n `166`; fx avg `0.0699` n `6`; index avg `-0.3762` n `27`; metal avg `-0.2749` n `20`; unknown avg `332.8763` n `1202`
- 24h: commodity avg `-0.4974` n `13`; crypto_alt avg `-1.6142` n `239`; crypto_major avg `-2.0659` n `8`; equity avg `0.4561` n `166`; fx avg `-0.1059` n `6`; index avg `0.1888` n `27`; metal avg `-0.4985` n `20`; unknown avg `-0.2033` n `1138`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
