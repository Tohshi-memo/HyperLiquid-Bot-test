# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T08:37:29.258043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.5932` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.4285` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.4076` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.0567` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1181` n `12`; crypto_alt avg `0.3947` n `228`; crypto_major avg `0.4428` n `8`; equity avg `0.1967` n `73`; fx avg `-0.0072` n `6`; index avg `0.0419` n `23`; metal avg `0.1671` n `18`; unknown avg `0.0521` n `424`
- 1h: commodity avg `0.0437` n `12`; crypto_alt avg `-0.6538` n `228`; crypto_major avg `-0.5143` n `8`; equity avg `-0.4899` n `73`; fx avg `0.0378` n `6`; index avg `-0.2242` n `23`; metal avg `0.1586` n `18`; unknown avg `-0.1041` n `424`
- 4h: commodity avg `-0.0746` n `12`; crypto_alt avg `-2.4387` n `228`; crypto_major avg `-2.6678` n `8`; equity avg `-0.6111` n `73`; fx avg `0.1255` n `6`; index avg `-0.2602` n `23`; metal avg `-0.2393` n `18`; unknown avg `0.0622` n `404`
- 24h: commodity avg `-0.6995` n `12`; crypto_alt avg `-6.2044` n `228`; crypto_major avg `-5.261` n `8`; equity avg `-3.9303` n `73`; fx avg `0.0719` n `6`; index avg `-1.2702` n `23`; metal avg `-0.964` n `18`; unknown avg `-0.9146` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
