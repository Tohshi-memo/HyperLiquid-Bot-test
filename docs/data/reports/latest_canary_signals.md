# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T22:52:36.278458+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.7648` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `3.43` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.6396` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0566` n `12`; crypto_alt avg `0.0138` n `228`; crypto_major avg `0.0097` n `8`; equity avg `0.0799` n `74`; fx avg `0.0134` n `6`; index avg `0.0033` n `23`; metal avg `0.1965` n `18`; unknown avg `13.0962` n `645`
- 1h: commodity avg `0.737` n `12`; crypto_alt avg `-0.2309` n `228`; crypto_major avg `-0.2022` n `8`; equity avg `0.045` n `74`; fx avg `0.0645` n `6`; index avg `-0.1667` n `23`; metal avg `0.8341` n `18`; unknown avg `-0.3937` n `645`
- 4h: commodity avg `-0.7732` n `12`; crypto_alt avg `3.0703` n `228`; crypto_major avg `2.9916` n `8`; equity avg `1.352` n `74`; fx avg `0.1362` n `6`; index avg `0.2615` n `23`; metal avg `1.6524` n `18`; unknown avg `3.5197` n `645`
- 24h: commodity avg `-0.7614` n `12`; crypto_alt avg `1.3437` n `228`; crypto_major avg `1.8681` n `8`; equity avg `1.4695` n `74`; fx avg `0.0935` n `6`; index avg `0.3635` n `23`; metal avg `1.5281` n `18`; unknown avg `1.2463` n `593`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
