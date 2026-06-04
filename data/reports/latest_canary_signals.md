# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T09:37:26.259744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.3463` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.9591` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.7976` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.1273` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `-1.5019` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.2188` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1338` n `12`; crypto_alt avg `-0.5889` n `228`; crypto_major avg `-0.2919` n `8`; equity avg `0.4387` n `73`; fx avg `0.0122` n `6`; index avg `0.0996` n `23`; metal avg `0.1574` n `18`; unknown avg `-0.0928` n `424`
- 1h: commodity avg `-0.1554` n `12`; crypto_alt avg `-1.867` n `228`; crypto_major avg `-1.388` n `8`; equity avg `-0.589` n `73`; fx avg `0.0136` n `6`; index avg `-0.1692` n `23`; metal avg `0.1139` n `18`; unknown avg `-0.8061` n `424`
- 4h: commodity avg `-0.2075` n `12`; crypto_alt avg `-3.2399` n `228`; crypto_major avg `-3.1666` n `8`; equity avg `-1.0393` n `73`; fx avg `0.1335` n `6`; index avg `-0.369` n `23`; metal avg `0.1797` n `18`; unknown avg `0.5402` n `404`
- 24h: commodity avg `-0.9991` n `12`; crypto_alt avg `-7.5776` n `228`; crypto_major avg `-6.4231` n `8`; equity avg `-4.3777` n `73`; fx avg `0.0754` n `6`; index avg `-1.4261` n `23`; metal avg `-0.7411` n `18`; unknown avg `-1.4745` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
