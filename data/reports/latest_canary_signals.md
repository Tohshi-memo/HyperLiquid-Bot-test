# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T10:07:23.162070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.2785` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.0704` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.6815` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.9983` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.2573` n `12`; crypto_alt avg `0.0047` n `228`; crypto_major avg `-0.219` n `8`; equity avg `0.0416` n `73`; fx avg `-0.0045` n `6`; index avg `-0.0319` n `23`; metal avg `-0.0434` n `18`; unknown avg `-0.2612` n `424`
- 1h: commodity avg `0.0827` n `12`; crypto_alt avg `-1.0423` n `228`; crypto_major avg `-0.7037` n `8`; equity avg `0.072` n `73`; fx avg `0.0307` n `6`; index avg `-0.0087` n `23`; metal avg `0.2082` n `18`; unknown avg `-0.5755` n `424`
- 4h: commodity avg `0.0019` n `12`; crypto_alt avg `-3.2572` n `228`; crypto_major avg `-3.0685` n `8`; equity avg `-1.0702` n `73`; fx avg `0.1283` n `6`; index avg `-0.387` n `23`; metal avg `0.21` n `18`; unknown avg `-1.6381` n `424`
- 24h: commodity avg `-0.8838` n `12`; crypto_alt avg `-7.8241` n `228`; crypto_major avg `-6.6999` n `8`; equity avg `-4.4126` n `73`; fx avg `0.0686` n `6`; index avg `-1.4817` n `23`; metal avg `-1.036` n `18`; unknown avg `-1.658` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
