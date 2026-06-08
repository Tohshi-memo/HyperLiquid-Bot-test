# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T01:07:21.968184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.8992` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.3006` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.2035` n `12`; crypto_alt avg `-0.7738` n `228`; crypto_major avg `-0.8251` n `8`; equity avg `-0.3118` n `74`; fx avg `-0.002` n `6`; index avg `-0.076` n `23`; metal avg `-0.3347` n `18`; unknown avg `0.08` n `517`
- 1h: commodity avg `-0.2668` n `12`; crypto_alt avg `0.246` n `228`; crypto_major avg `0.2809` n `8`; equity avg `0.4548` n `74`; fx avg `-0.0311` n `6`; index avg `0.1969` n `23`; metal avg `-0.2705` n `18`; unknown avg `-0.2605` n `517`
- 4h: commodity avg `-0.4304` n `12`; crypto_alt avg `1.9842` n `228`; crypto_major avg `2.4688` n `8`; equity avg `1.1313` n `74`; fx avg `-0.062` n `6`; index avg `0.2549` n `23`; metal avg `0.1682` n `18`; unknown avg `0.4105` n `516`
- 24h: commodity avg `-0.2195` n `12`; crypto_alt avg `2.33` n `228`; crypto_major avg `4.555` n `8`; equity avg `1.9138` n `74`; fx avg `-0.0957` n `6`; index avg `0.6011` n `23`; metal avg `0.3957` n `18`; unknown avg `-4.5678` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
