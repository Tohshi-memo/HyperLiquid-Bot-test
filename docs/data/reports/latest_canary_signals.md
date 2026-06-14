# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T22:37:27.727970+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.7273` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `3.18` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.7887` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6498` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1749` n `12`; crypto_alt avg `0.1335` n `228`; crypto_major avg `0.0703` n `8`; equity avg `-0.0356` n `74`; fx avg `-0.0081` n `6`; index avg `-0.1013` n `23`; metal avg `-0.3434` n `18`; unknown avg `-0.1581` n `645`
- 1h: commodity avg `0.1984` n `12`; crypto_alt avg `0.7407` n `228`; crypto_major avg `0.9285` n `8`; equity avg `0.3305` n `74`; fx avg `0.0415` n `6`; index avg `0.1248` n `23`; metal avg `1.0561` n `18`; unknown avg `1.8449` n `645`
- 4h: commodity avg `-0.6216` n `12`; crypto_alt avg `3.1705` n `228`; crypto_major avg `3.1057` n `8`; equity avg `1.317` n `74`; fx avg `0.1057` n `6`; index avg `0.2513` n `23`; metal avg `1.4559` n `18`; unknown avg `3.2745` n `645`
- 24h: commodity avg `-0.7699` n `12`; crypto_alt avg `1.2307` n `228`; crypto_major avg `1.8504` n `8`; equity avg `1.3889` n `74`; fx avg `0.0967` n `6`; index avg `0.3649` n `23`; metal avg `1.3262` n `18`; unknown avg `1.2396` n `593`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
