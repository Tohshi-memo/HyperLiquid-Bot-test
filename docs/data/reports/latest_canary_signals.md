# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T07:22:28.381516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.2855` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.8491` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.5599` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.2449` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1163` n `12`; crypto_alt avg `0.3714` n `228`; crypto_major avg `0.3816` n `8`; equity avg `0.0503` n `74`; fx avg `0.0346` n `6`; index avg `0.0452` n `23`; metal avg `0.1252` n `18`; unknown avg `1.1495` n `424`
- 1h: commodity avg `-0.3268` n `12`; crypto_alt avg `-0.0749` n `228`; crypto_major avg `0.2071` n `8`; equity avg `-0.2028` n `74`; fx avg `0.0121` n `6`; index avg `-0.0612` n `23`; metal avg `0.6453` n `18`; unknown avg `1.4558` n `424`
- 4h: commodity avg `-0.4195` n `12`; crypto_alt avg `-3.4009` n `228`; crypto_major avg `-2.9794` n `8`; equity avg `-0.7345` n `74`; fx avg `0.019` n `6`; index avg `-0.1303` n `23`; metal avg `0.3061` n `18`; unknown avg `0.3609` n `404`
- 24h: commodity avg `-0.5132` n `12`; crypto_alt avg `-7.1401` n `228`; crypto_major avg `-5.6426` n `8`; equity avg `-2.02` n `73`; fx avg `0.1322` n `6`; index avg `-0.6339` n `23`; metal avg `-0.224` n `18`; unknown avg `-1.3511` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
