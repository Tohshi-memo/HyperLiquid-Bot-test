# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T07:37:22.476880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.2225` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.1708` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.1667` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-2.0957` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.3136` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0185` n `12`; crypto_alt avg `0.1819` n `228`; crypto_major avg `0.2249` n `8`; equity avg `0.2281` n `73`; fx avg `0.002` n `6`; index avg `0.0168` n `23`; metal avg `0.0635` n `18`; unknown avg `0.0842` n `424`
- 1h: commodity avg `0.0978` n `12`; crypto_alt avg `-1.488` n `228`; crypto_major avg `-1.3366` n `8`; equity avg `-0.0512` n `73`; fx avg `0.0585` n `6`; index avg `-0.023` n `23`; metal avg `0.0148` n `18`; unknown avg `0.4298` n `424`
- 4h: commodity avg `-0.0141` n `12`; crypto_alt avg `-2.4335` n `228`; crypto_major avg `-2.1849` n `8`; equity avg `-0.0182` n `73`; fx avg `0.0846` n `6`; index avg `0.0376` n `23`; metal avg `-0.0892` n `18`; unknown avg `0.392` n `404`
- 24h: commodity avg `-0.4617` n `12`; crypto_alt avg `-5.6989` n `228`; crypto_major avg `-5.0178` n `8`; equity avg `-3.5408` n `73`; fx avg `0.0071` n `6`; index avg `-1.0606` n `23`; metal avg `-1.1348` n `18`; unknown avg `0.419` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1648`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
