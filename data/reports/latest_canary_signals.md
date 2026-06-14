# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T21:37:28.246649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6294` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `2.2959` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5798` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.092` n `12`; crypto_alt avg `0.5485` n `228`; crypto_major avg `0.4891` n `8`; equity avg `0.5327` n `74`; fx avg `0.0825` n `6`; index avg `0.0714` n `23`; metal avg `0.1199` n `18`; unknown avg `-0.027` n `645`
- 1h: commodity avg `-0.7312` n `12`; crypto_alt avg `1.6868` n `228`; crypto_major avg `1.5647` n `8`; equity avg `0.843` n `74`; fx avg `0.057` n `6`; index avg `0.1268` n `23`; metal avg `0.3225` n `18`; unknown avg `0.9772` n `645`
- 4h: commodity avg `-0.6716` n `12`; crypto_alt avg `2.0537` n `228`; crypto_major avg `1.9578` n `8`; equity avg `0.9077` n `74`; fx avg `0.0591` n `6`; index avg `0.1242` n `23`; metal avg `0.378` n `18`; unknown avg `0.978` n `645`
- 24h: commodity avg `-0.9784` n `12`; crypto_alt avg `0.9298` n `228`; crypto_major avg `1.1906` n `8`; equity avg `1.1146` n `74`; fx avg `0.0119` n `6`; index avg `0.1197` n `23`; metal avg `-0.4296` n `18`; unknown avg `1.3432` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
