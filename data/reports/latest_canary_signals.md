# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T18:52:18.087577+00:00`
- Correlation status: `ready`
- Asset price records: `575`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0258` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.6127` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5083` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1984` n `12`; crypto_alt avg `-0.4438` n `228`; crypto_major avg `-0.3599` n `8`; equity avg `-0.2778` n `65`; fx avg `0.0096` n `5`; index avg `-0.1473` n `23`; metal avg `-0.3933` n `18`; unknown avg `0.7192` n `365`
- 1h: commodity avg `-0.1216` n `12`; crypto_alt avg `0.518` n `228`; crypto_major avg `0.0615` n `8`; equity avg `-0.1551` n `65`; fx avg `-0.0069` n `5`; index avg `-0.089` n `23`; metal avg `-0.2686` n `18`; unknown avg `0.8171` n `365`
- 4h: commodity avg `1.737` n `12`; crypto_alt avg `0.7524` n `228`; crypto_major avg `-0.2888` n `8`; equity avg `-1.7971` n `65`; fx avg `0.062` n `5`; index avg `-1.0008` n `23`; metal avg `-1.9015` n `18`; unknown avg `0.6936` n `365`
- 24h: commodity avg `0.6306` n `12`; crypto_alt avg `1.2456` n `228`; crypto_major avg `-1.753` n `8`; equity avg `-1.23` n `65`; fx avg `0.2` n `5`; index avg `-0.8659` n `23`; metal avg `0.1865` n `18`; unknown avg `0.8375` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1373`, n `571`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1152`, n `571`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1025`, n `571`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0925`, n `571`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `567`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0919`, n `567`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `567`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0882`, n `567`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0873`, n `567`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0775`, n `567`, weak_sample_signal
