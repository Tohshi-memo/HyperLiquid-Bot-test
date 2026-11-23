# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T20:07:29.808563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.7797` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.5856` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.4585` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0014` n `13`; crypto_alt avg `-0.0552` n `239`; crypto_major avg `-0.1041` n `8`; equity avg `-0.0741` n `166`; fx avg `0.0045` n `6`; index avg `0.0113` n `27`; metal avg `0.0138` n `20`; unknown avg `167.6256` n `1250`
- 1h: commodity avg `-0.1753` n `13`; crypto_alt avg `-0.8457` n `239`; crypto_major avg `-0.7973` n `8`; equity avg `-0.6616` n `166`; fx avg `-0.0063` n `6`; index avg `-0.0783` n `27`; metal avg `-0.1166` n `20`; unknown avg `166.7627` n `1256`
- 4h: commodity avg `0.0843` n `13`; crypto_alt avg `-2.2163` n `239`; crypto_major avg `-2.6954` n `8`; equity avg `-1.2273` n `166`; fx avg `-0.0616` n `6`; index avg `-0.1098` n `27`; metal avg `-0.2369` n `20`; unknown avg `323.5666` n `1258`
- 24h: commodity avg `-1.5567` n `13`; crypto_alt avg `1.5051` n `239`; crypto_major avg `1.7297` n `8`; equity avg `5.3844` n `166`; fx avg `-0.086` n `6`; index avg `0.5214` n `27`; metal avg `0.579` n `20`; unknown avg `331.3425` n `1068`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
