# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T04:37:20.787402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.3327` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.9557` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.6642` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `2.1198` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.0669` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-1.9268` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-1.7126` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `-1.5621` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1261` n `12`; crypto_alt avg `-1.0151` n `228`; crypto_major avg `-0.7013` n `8`; equity avg `-0.356` n `74`; fx avg `-0.0069` n `6`; index avg `-0.3407` n `23`; metal avg `-0.0993` n `18`; unknown avg `-0.6287` n `425`
- 1h: commodity avg `-0.1676` n `12`; crypto_alt avg `-2.9759` n `228`; crypto_major avg `-2.2345` n `8`; equity avg `-0.5219` n `74`; fx avg `0.0219` n `6`; index avg `-0.1147` n `23`; metal avg `-0.3077` n `18`; unknown avg `-1.1022` n `425`
- 4h: commodity avg `-0.3075` n `12`; crypto_alt avg `-4.9759` n `228`; crypto_major avg `-3.6402` n `8`; equity avg `-2.0781` n `74`; fx avg `-0.0216` n `6`; index avg `-0.976` n `23`; metal avg `-0.6845` n `18`; unknown avg `-0.778` n `425`
- 24h: commodity avg `-1.3985` n `12`; crypto_alt avg `-8.9418` n `228`; crypto_major avg `-7.2579` n `8`; equity avg `-7.173` n `74`; fx avg `-0.1913` n `6`; index avg `-4.2595` n `23`; metal avg `-4.348` n `18`; unknown avg `-1.3423` n `404`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
