# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T08:37:21.462499+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.6429` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.1143` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.0525` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0119` n `12`; crypto_alt avg `0.367` n `228`; crypto_major avg `0.3308` n `8`; equity avg `0.0295` n `74`; fx avg `0.0` n `6`; index avg `-0.0359` n `23`; metal avg `0.028` n `18`; unknown avg `-0.0715` n `425`
- 1h: commodity avg `0.0506` n `12`; crypto_alt avg `0.8378` n `228`; crypto_major avg `0.6827` n `8`; equity avg `-0.123` n `74`; fx avg `0.0017` n `6`; index avg `-0.149` n `23`; metal avg `0.005` n `18`; unknown avg `0.2698` n `425`
- 4h: commodity avg `-0.1822` n `12`; crypto_alt avg `4.0491` n `228`; crypto_major avg `3.4607` n `8`; equity avg `0.4082` n `74`; fx avg `-0.021` n `6`; index avg `0.1458` n `23`; metal avg `0.3464` n `18`; unknown avg `0.7182` n `415`
- 24h: commodity avg `-1.0615` n `12`; crypto_alt avg `-2.4592` n `228`; crypto_major avg `-2.2446` n `8`; equity avg `-6.8662` n `74`; fx avg `-0.242` n `6`; index avg `-4.2325` n `23`; metal avg `-4.1107` n `18`; unknown avg `0.682` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
