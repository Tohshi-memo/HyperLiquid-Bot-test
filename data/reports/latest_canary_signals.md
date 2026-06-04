# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T08:52:25.687192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2973` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.1452` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.0545` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.5915` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0864` n `12`; crypto_alt avg `0.1345` n `228`; crypto_major avg `0.0901` n `8`; equity avg `-0.3243` n `73`; fx avg `-0.0004` n `6`; index avg `-0.0889` n `23`; metal avg `-0.0958` n `18`; unknown avg `-0.1903` n `424`
- 1h: commodity avg `-0.1971` n `12`; crypto_alt avg `-0.3088` n `228`; crypto_major avg `-0.2008` n `8`; equity avg `-0.6516` n `73`; fx avg `0.035` n `6`; index avg `-0.3167` n `23`; metal avg `0.1114` n `18`; unknown avg `0.0747` n `424`
- 4h: commodity avg `-0.1302` n `12`; crypto_alt avg `-2.1281` n `228`; crypto_major avg `-2.4275` n `8`; equity avg `-0.836` n `73`; fx avg `0.1166` n `6`; index avg `-0.373` n `23`; metal avg `-0.2823` n `18`; unknown avg `-0.8205` n `404`
- 24h: commodity avg `-0.8317` n `12`; crypto_alt avg `-6.0581` n `228`; crypto_major avg `-5.2245` n `8`; equity avg `-4.2964` n `73`; fx avg `0.0875` n `6`; index avg `-1.3229` n `23`; metal avg `-0.9388` n `18`; unknown avg `-1.1256` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
