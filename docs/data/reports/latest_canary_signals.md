# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T08:07:25.653842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `2.2023` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `2.1824` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `1.7149` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.535` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5121` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1163` n `12`; crypto_alt avg `-0.3028` n `228`; crypto_major avg `-0.1574` n `8`; equity avg `0.0054` n `74`; fx avg `0.0176` n `6`; index avg `-0.08` n `23`; metal avg `-0.1631` n `18`; unknown avg `0.0622` n `424`
- 1h: commodity avg `-0.0033` n `12`; crypto_alt avg `1.8766` n `228`; crypto_major avg `2.1791` n `8`; equity avg `0.4642` n `74`; fx avg `0.047` n `6`; index avg `0.108` n `23`; metal avg `-0.0232` n `18`; unknown avg `1.8965` n `424`
- 4h: commodity avg `-0.238` n `12`; crypto_alt avg `-2.2429` n `228`; crypto_major avg `-1.5244` n `8`; equity avg `-0.2038` n `74`; fx avg `0.0207` n `6`; index avg `0.0106` n `23`; metal avg `-0.0123` n `18`; unknown avg `-0.0063` n `404`
- 24h: commodity avg `-0.5033` n `12`; crypto_alt avg `-5.4842` n `228`; crypto_major avg `-3.7738` n `8`; equity avg `-1.6487` n `73`; fx avg `0.1022` n `6`; index avg `-0.5528` n `23`; metal avg `-0.5029` n `18`; unknown avg `0.4581` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
