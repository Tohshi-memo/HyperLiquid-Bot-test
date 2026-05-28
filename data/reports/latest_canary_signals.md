# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T09:37:22.849107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `0.1308` n `228`; crypto_major avg `0.1287` n `8`; equity avg `-0.0475` n `67`; fx avg `-0.0067` n `6`; index avg `-0.0176` n `23`; metal avg `-0.1038` n `18`; unknown avg `-0.043` n `419`
- 1h: commodity avg `-0.0668` n `12`; crypto_alt avg `0.032` n `228`; crypto_major avg `0.2054` n `8`; equity avg `-0.0291` n `67`; fx avg `-0.0064` n `6`; index avg `-0.0298` n `23`; metal avg `0.0112` n `18`; unknown avg `0.0089` n `419`
- 4h: commodity avg `-0.3627` n `12`; crypto_alt avg `0.389` n `228`; crypto_major avg `0.4003` n `8`; equity avg `0.5769` n `67`; fx avg `0.0035` n `6`; index avg `0.2139` n `23`; metal avg `0.3605` n `18`; unknown avg `0.1506` n `409`
- 24h: commodity avg `0.5549` n `12`; crypto_alt avg `-4.6616` n `228`; crypto_major avg `-3.7003` n `8`; equity avg `-1.5127` n `67`; fx avg `-0.0991` n `6`; index avg `-0.9788` n `23`; metal avg `-1.6627` n `18`; unknown avg `-1.5873` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1724`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
