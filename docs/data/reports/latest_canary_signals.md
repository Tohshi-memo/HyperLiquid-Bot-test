# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T08:52:25.180788+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.2557` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.1429` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `0.0941` n `231`; crypto_major avg `0.1913` n `8`; equity avg `0.1227` n `127`; fx avg `-0.0041` n `6`; index avg `0.0079` n `26`; metal avg `-0.0132` n `20`; unknown avg `-0.0659` n `792`
- 1h: commodity avg `0.0798` n `12`; crypto_alt avg `1.27` n `231`; crypto_major avg `1.3712` n `8`; equity avg `0.5701` n `127`; fx avg `-0.0115` n `6`; index avg `0.0677` n `26`; metal avg `0.0049` n `20`; unknown avg `0.0467` n `792`
- 4h: commodity avg `-0.1078` n `12`; crypto_alt avg `1.8485` n `231`; crypto_major avg `2.0351` n `8`; equity avg `0.8526` n `127`; fx avg `-0.0161` n `6`; index avg `0.084` n `26`; metal avg `-0.2206` n `20`; unknown avg `0.2163` n `775`
- 24h: commodity avg `0.4656` n `12`; crypto_alt avg `1.7075` n `231`; crypto_major avg `2.2507` n `8`; equity avg `2.1528` n `127`; fx avg `-0.1002` n `6`; index avg `0.3198` n `26`; metal avg `-0.3454` n `20`; unknown avg `0.4111` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
