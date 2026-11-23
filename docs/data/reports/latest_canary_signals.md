# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T18:37:28.956736+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `3.7258` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-3.3951` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.3906` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.7413` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0427` n `13`; crypto_alt avg `-0.0177` n `239`; crypto_major avg `0.0654` n `8`; equity avg `-0.2368` n `166`; fx avg `-0.0023` n `6`; index avg `-0.0092` n `27`; metal avg `-0.0716` n `20`; unknown avg `0.0525` n `1266`
- 1h: commodity avg `0.0502` n `13`; crypto_alt avg `-0.3946` n `239`; crypto_major avg `-0.5333` n `8`; equity avg `-0.337` n `166`; fx avg `-0.0117` n `6`; index avg `-0.0327` n `27`; metal avg `-0.137` n `20`; unknown avg `362.6433` n `1266`
- 4h: commodity avg `-0.3487` n `13`; crypto_alt avg `-2.593` n `239`; crypto_major avg `-3.7438` n `8`; equity avg `-1.0025` n `166`; fx avg `-0.1281` n `6`; index avg `-0.018` n `27`; metal avg `-0.3532` n `20`; unknown avg `7.7687` n `1258`
- 24h: commodity avg `-1.2903` n `13`; crypto_alt avg `2.772` n `239`; crypto_major avg `2.3016` n `8`; equity avg `5.929` n `166`; fx avg `-0.0882` n `6`; index avg `0.5471` n `27`; metal avg `0.609` n `20`; unknown avg `187.1522` n `1064`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
