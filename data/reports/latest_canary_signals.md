# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T02:22:21.056660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.6838` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.9352` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.6482` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.4062` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0272` n `12`; crypto_alt avg `0.7963` n `228`; crypto_major avg `0.7007` n `8`; equity avg `0.0084` n `73`; fx avg `-0.023` n `6`; index avg `-0.03` n `23`; metal avg `0.036` n `18`; unknown avg `0.2262` n `420`
- 1h: commodity avg `-0.1844` n `12`; crypto_alt avg `-2.0616` n `228`; crypto_major avg `-0.5145` n `8`; equity avg `-0.4326` n `73`; fx avg `-0.0124` n `6`; index avg `-0.2457` n `23`; metal avg `-0.3427` n `18`; unknown avg `0.4302` n `420`
- 4h: commodity avg `-0.5021` n `12`; crypto_alt avg `-5.13` n `228`; crypto_major avg `-3.1503` n `8`; equity avg `-0.7441` n `73`; fx avg `-0.0224` n `6`; index avg `-0.2151` n `23`; metal avg `0.5335` n `18`; unknown avg `-0.9294` n `419`
- 24h: commodity avg `-0.0509` n `12`; crypto_alt avg `-3.2961` n `228`; crypto_major avg `-3.5551` n `8`; equity avg `-3.9548` n `73`; fx avg `0.0083` n `6`; index avg `-1.3379` n `23`; metal avg `-1.5895` n `18`; unknown avg `0.8919` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
