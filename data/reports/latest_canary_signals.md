# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T23:07:32.309955+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5045` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.2524` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.003` n `13`; crypto_alt avg `0.3399` n `239`; crypto_major avg `0.3591` n `8`; equity avg `-0.0563` n `166`; fx avg `0.0071` n `6`; index avg `-0.0111` n `27`; metal avg `0.049` n `20`; unknown avg `0.2321` n `1258`
- 1h: commodity avg `0.0107` n `13`; crypto_alt avg `-0.177` n `239`; crypto_major avg `-0.0778` n `8`; equity avg `0.2267` n `166`; fx avg `0.0292` n `6`; index avg `0.0259` n `27`; metal avg `0.0722` n `20`; unknown avg `0.1507` n `1262`
- 4h: commodity avg `-0.0687` n `13`; crypto_alt avg `-1.7151` n `239`; crypto_major avg `-1.2187` n `8`; equity avg `0.2858` n `166`; fx avg `0.0073` n `6`; index avg `0.0337` n `27`; metal avg `-0.0605` n `20`; unknown avg `338.5777` n `1220`
- 24h: commodity avg `-1.2455` n `13`; crypto_alt avg `0.7394` n `239`; crypto_major avg `1.0419` n `8`; equity avg `6.6719` n `166`; fx avg `-0.1708` n `6`; index avg `0.7` n `27`; metal avg `0.4779` n `20`; unknown avg `309.1092` n `1054`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
