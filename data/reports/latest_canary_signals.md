# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T06:37:17.115557+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1038` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.4204` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0562` n `12`; crypto_alt avg `-0.327` n `228`; crypto_major avg `-0.2488` n `8`; equity avg `-0.1288` n `67`; fx avg `-0.0003` n `6`; index avg `-0.065` n `23`; metal avg `0.1259` n `18`; unknown avg `0.0811` n `419`
- 1h: commodity avg `-0.1471` n `12`; crypto_alt avg `-0.2204` n `228`; crypto_major avg `-0.2398` n `8`; equity avg `0.3111` n `67`; fx avg `-0.006` n `6`; index avg `0.0874` n `23`; metal avg `0.1592` n `18`; unknown avg `0.0169` n `409`
- 4h: commodity avg `0.3634` n `12`; crypto_alt avg `-3.0458` n `228`; crypto_major avg `-1.7404` n `8`; equity avg `-0.4823` n `67`; fx avg `-0.0721` n `6`; index avg `-0.32` n `23`; metal avg `-0.3784` n `18`; unknown avg `-0.813` n `409`
- 24h: commodity avg `0.0239` n `12`; crypto_alt avg `-5.4806` n `228`; crypto_major avg `-4.1048` n `8`; equity avg `-1.1254` n `67`; fx avg `-0.1359` n `6`; index avg `-0.9147` n `23`; metal avg `-1.5773` n `18`; unknown avg `-1.8571` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
