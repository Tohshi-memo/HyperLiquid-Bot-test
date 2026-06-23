# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T09:37:29.457358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2288` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.2088` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.1313` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.9062` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0736` n `12`; crypto_alt avg `-0.108` n `228`; crypto_major avg `-0.1256` n `8`; equity avg `0.0199` n `86`; fx avg `-0.0047` n `6`; index avg `0.0125` n `23`; metal avg `0.0956` n `20`; unknown avg `-0.0423` n `764`
- 1h: commodity avg `-0.1538` n `12`; crypto_alt avg `0.3967` n `228`; crypto_major avg `-0.016` n `8`; equity avg `0.46` n `86`; fx avg `-0.0057` n `6`; index avg `0.0679` n `23`; metal avg `0.2287` n `20`; unknown avg `-0.0833` n `764`
- 4h: commodity avg `-0.1125` n `12`; crypto_alt avg `-2.1963` n `228`; crypto_major avg `-2.3413` n `8`; equity avg `-0.4351` n `86`; fx avg `-0.0234` n `6`; index avg `-0.1325` n `23`; metal avg `-0.21` n `20`; unknown avg `-0.6184` n `604`
- 24h: commodity avg `-0.7012` n `12`; crypto_alt avg `-3.7259` n `228`; crypto_major avg `-4.0073` n `8`; equity avg `-4.2038` n `85`; fx avg `-0.108` n `6`; index avg `-0.7844` n `23`; metal avg `-1.4068` n `18`; unknown avg `0.6797` n `583`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
