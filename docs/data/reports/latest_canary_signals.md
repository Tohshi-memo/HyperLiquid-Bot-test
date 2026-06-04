# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T08:58:24.786637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0815` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.966` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8246` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0921` n `12`; crypto_alt avg `0.4241` n `228`; crypto_major avg `0.3076` n `8`; equity avg `-0.2569` n `73`; fx avg `0.0041` n `6`; index avg `-0.1083` n `23`; metal avg `-0.0647` n `18`; unknown avg `-0.3527` n `424`
- 1h: commodity avg `-0.2028` n `12`; crypto_alt avg `-0.021` n `228`; crypto_major avg `0.0158` n `8`; equity avg `-0.5844` n `73`; fx avg `0.0395` n `6`; index avg `-0.336` n `23`; metal avg `0.1426` n `18`; unknown avg `-0.1708` n `424`
- 4h: commodity avg `-0.1358` n `12`; crypto_alt avg `-1.8486` n `228`; crypto_major avg `-2.2173` n `8`; equity avg `-0.77` n `73`; fx avg `0.1211` n `6`; index avg `-0.3927` n `23`; metal avg `-0.2513` n `18`; unknown avg `-1.0812` n `404`
- 24h: commodity avg `-0.8371` n `12`; crypto_alt avg `-5.7946` n `228`; crypto_major avg `-5.0204` n `8`; equity avg `-4.2349` n `73`; fx avg `0.092` n `6`; index avg `-1.3414` n `23`; metal avg `-0.9078` n `18`; unknown avg `-1.5036` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
