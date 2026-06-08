# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T14:52:33.320208+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2274` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0265` n `12`; crypto_alt avg `0.312` n `228`; crypto_major avg `0.2582` n `8`; equity avg `0.3555` n `74`; fx avg `0.0075` n `6`; index avg `0.1936` n `23`; metal avg `0.2172` n `18`; unknown avg `0.0326` n `517`
- 1h: commodity avg `0.3058` n `12`; crypto_alt avg `0.1271` n `228`; crypto_major avg `0.2563` n `8`; equity avg `0.804` n `74`; fx avg `-0.0078` n `6`; index avg `0.1644` n `23`; metal avg `-0.1105` n `18`; unknown avg `-0.2286` n `517`
- 4h: commodity avg `-0.5292` n `12`; crypto_alt avg `1.2891` n `228`; crypto_major avg `1.6982` n `8`; equity avg `1.8227` n `74`; fx avg `-0.0071` n `6`; index avg `0.7568` n `23`; metal avg `0.3792` n `18`; unknown avg `-1.6772` n `517`
- 24h: commodity avg `-0.2032` n `12`; crypto_alt avg `2.0023` n `228`; crypto_major avg `3.5191` n `8`; equity avg `2.6436` n `74`; fx avg `-0.2786` n `6`; index avg `0.9982` n `23`; metal avg `-0.1366` n `18`; unknown avg `-2.863` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
