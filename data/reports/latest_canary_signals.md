# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T01:22:22.063600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.9948` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `-2.6272` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.2748` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `2.2427` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_equity_divergence: score `-2.1942` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `-1.929` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0921` n `12`; crypto_alt avg `-1.6773` n `228`; crypto_major avg `-1.3136` n `8`; equity avg `-0.268` n `73`; fx avg `0.0128` n `6`; index avg `-0.0073` n `23`; metal avg `0.2561` n `18`; unknown avg `-0.6414` n `420`
- 1h: commodity avg `-0.205` n `12`; crypto_alt avg `-2.8358` n `228`; crypto_major avg `-2.1645` n `8`; equity avg `0.0297` n `73`; fx avg `0.0488` n `6`; index avg `0.1103` n `23`; metal avg `0.4627` n `18`; unknown avg `-0.5102` n `419`
- 4h: commodity avg `-0.5971` n `12`; crypto_alt avg `-2.4764` n `228`; crypto_major avg `-2.3537` n `8`; equity avg `-0.4247` n `73`; fx avg `-0.0147` n `6`; index avg `-0.111` n `23`; metal avg `0.6411` n `18`; unknown avg `-0.3578` n `419`
- 24h: commodity avg `-0.021` n `12`; crypto_alt avg `-1.5878` n `228`; crypto_major avg `-3.4776` n `8`; equity avg `-3.5018` n `72`; fx avg `0.0046` n `6`; index avg `-1.0901` n `23`; metal avg `-1.1553` n `18`; unknown avg `0.4529` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
