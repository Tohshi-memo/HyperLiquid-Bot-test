# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T22:33:19.787526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `1.7218` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.094` n `12`; crypto_alt avg `-0.4753` n `228`; crypto_major avg `-0.4242` n `8`; equity avg `-0.0324` n `74`; fx avg `-0.0046` n `6`; index avg `-0.1363` n `23`; metal avg `-0.0837` n `18`; unknown avg `0.0607` n `516`
- 1h: commodity avg `-0.1513` n `12`; crypto_alt avg `2.0366` n `228`; crypto_major avg `1.6449` n `8`; equity avg `0.2172` n `74`; fx avg `-0.0173` n `6`; index avg `-0.1781` n `23`; metal avg `-0.0769` n `18`; unknown avg `0.3091` n `516`
- 4h: commodity avg `0.061` n `12`; crypto_alt avg `0.7512` n `228`; crypto_major avg `0.7009` n `8`; equity avg `-0.0669` n `74`; fx avg `-0.0282` n `6`; index avg `-0.1315` n `23`; metal avg `-0.332` n `18`; unknown avg `0.0537` n `516`
- 24h: commodity avg `0.3707` n `12`; crypto_alt avg `3.5604` n `228`; crypto_major avg `4.8722` n `8`; equity avg `1.6106` n `74`; fx avg `-0.0657` n `6`; index avg `0.1679` n `23`; metal avg `0.2595` n `18`; unknown avg `-4.4395` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
