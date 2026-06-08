# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T13:22:28.021070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5563` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `1.5236` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1311` n `12`; crypto_alt avg `0.0287` n `228`; crypto_major avg `0.2913` n `8`; equity avg `0.0179` n `74`; fx avg `0.0177` n `6`; index avg `-0.1366` n `23`; metal avg `0.1237` n `18`; unknown avg `0.0013` n `517`
- 1h: commodity avg `-0.0712` n `12`; crypto_alt avg `0.9202` n `228`; crypto_major avg `1.4235` n `8`; equity avg `0.5691` n `74`; fx avg `0.0194` n `6`; index avg `0.1392` n `23`; metal avg `-0.1001` n `18`; unknown avg `0.789` n `517`
- 4h: commodity avg `-1.06` n `12`; crypto_alt avg `1.4957` n `228`; crypto_major avg `1.4963` n `8`; equity avg `1.5361` n `74`; fx avg `0.0705` n `6`; index avg `0.7188` n `23`; metal avg `0.8581` n `18`; unknown avg `-1.5362` n `517`
- 24h: commodity avg `-0.5156` n `12`; crypto_alt avg `3.1192` n `228`; crypto_major avg `4.288` n `8`; equity avg `2.8497` n `74`; fx avg `-0.2679` n `6`; index avg `1.1813` n `23`; metal avg `0.2895` n `18`; unknown avg `-2.7345` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
