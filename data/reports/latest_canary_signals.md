# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T14:37:29.227263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2596` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.1985` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.4051` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0099` n `13`; crypto_alt avg `0.094` n `239`; crypto_major avg `-0.2956` n `8`; equity avg `-0.1329` n `166`; fx avg `0.0047` n `6`; index avg `-0.0155` n `27`; metal avg `-0.0092` n `20`; unknown avg `219.0905` n `1262`
- 1h: commodity avg `0.0168` n `13`; crypto_alt avg `0.2977` n `239`; crypto_major avg `-0.0918` n `8`; equity avg `-0.0838` n `166`; fx avg `0.0077` n `6`; index avg `-0.0014` n `27`; metal avg `-0.0567` n `20`; unknown avg `183.7409` n `1262`
- 4h: commodity avg `0.0687` n `13`; crypto_alt avg `2.8` n `239`; crypto_major avg `3.3283` n `8`; equity avg `0.9232` n `166`; fx avg `0.0299` n `6`; index avg `0.112` n `27`; metal avg `0.1298` n `20`; unknown avg `0.7981` n `1220`
- 24h: commodity avg `0.6084` n `13`; crypto_alt avg `-2.0115` n `239`; crypto_major avg `-2.411` n `8`; equity avg `-3.4984` n `166`; fx avg `-0.1033` n `6`; index avg `-0.4038` n `27`; metal avg `-0.2537` n `20`; unknown avg `0.3544` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
