# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T19:22:39.350138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.2044` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.1106` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.9329` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.0402` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1461` n `13`; crypto_alt avg `-0.3411` n `239`; crypto_major avg `-0.2511` n `8`; equity avg `-0.01` n `166`; fx avg `-0.0152` n `6`; index avg `-0.0008` n `27`; metal avg `-0.0217` n `20`; unknown avg `0.0938` n `1264`
- 1h: commodity avg `-0.2127` n `13`; crypto_alt avg `-0.4389` n `239`; crypto_major avg `-0.1522` n `8`; equity avg `-0.1809` n `166`; fx avg `-0.0082` n `6`; index avg `0.0067` n `27`; metal avg `-0.0432` n `20`; unknown avg `0.8282` n `1264`
- 4h: commodity avg `-0.0158` n `13`; crypto_alt avg `-2.3196` n `239`; crypto_major avg `-3.2202` n `8`; equity avg `-1.18` n `166`; fx avg `-0.0815` n `6`; index avg `-0.1096` n `27`; metal avg `-0.2873` n `20`; unknown avg `7.3605` n `1258`
- 24h: commodity avg `-1.5344` n `13`; crypto_alt avg `1.9256` n `239`; crypto_major avg `2.2209` n `8`; equity avg `6.1122` n `166`; fx avg `-0.0927` n `6`; index avg `0.5891` n `27`; metal avg `0.6786` n `20`; unknown avg `241.47` n `1060`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
