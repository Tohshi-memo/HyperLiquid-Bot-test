# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T15:37:25.588218+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2556` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.1317` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.1221` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-1.7043` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6062` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.3145` n `12`; crypto_alt avg `-0.7532` n `228`; crypto_major avg `-0.8514` n `8`; equity avg `-0.3033` n `74`; fx avg `-0.0282` n `6`; index avg `-0.1829` n `23`; metal avg `-0.1502` n `18`; unknown avg `0.7396` n `424`
- 1h: commodity avg `-0.3675` n `12`; crypto_alt avg `-2.4937` n `228`; crypto_major avg `-2.4896` n `8`; equity avg `-1.4699` n `74`; fx avg `-0.0364` n `6`; index avg `-0.3579` n `23`; metal avg `-0.7853` n `18`; unknown avg `0.2404` n `424`
- 4h: commodity avg `-1.0075` n `12`; crypto_alt avg `-2.8893` n `228`; crypto_major avg `-3.2631` n `8`; equity avg `-3.4174` n `74`; fx avg `-0.181` n `6`; index avg `-1.6569` n `23`; metal avg `-3.2903` n `18`; unknown avg `1.5027` n `424`
- 24h: commodity avg `-1.2512` n `12`; crypto_alt avg `-9.2704` n `228`; crypto_major avg `-7.3065` n `8`; equity avg `-5.129` n `74`; fx avg `-0.0277` n `6`; index avg `-2.2401` n `23`; metal avg `-3.8932` n `18`; unknown avg `-0.1674` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
