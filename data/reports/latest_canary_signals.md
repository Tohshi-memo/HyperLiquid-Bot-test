# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T23:07:30.670213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.9307` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `3.55` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.7417` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1695` n `12`; crypto_alt avg `-0.0901` n `228`; crypto_major avg `-0.028` n `8`; equity avg `-0.163` n `74`; fx avg `-0.0122` n `6`; index avg `-0.0359` n `23`; metal avg `-0.0509` n `18`; unknown avg `0.0896` n `645`
- 1h: commodity avg `0.1228` n `12`; crypto_alt avg `0.2617` n `228`; crypto_major avg `0.521` n `8`; equity avg `-0.0562` n `74`; fx avg `-0.0144` n `6`; index avg `-0.1052` n `23`; metal avg `-0.4167` n `18`; unknown avg `6.9097` n `645`
- 4h: commodity avg `-1.0396` n `12`; crypto_alt avg `2.8693` n `228`; crypto_major avg `2.8911` n `8`; equity avg `1.1494` n `74`; fx avg `0.1386` n `6`; index avg `0.2258` n `23`; metal avg `1.6277` n `18`; unknown avg `2.956` n `645`
- 24h: commodity avg `-0.8718` n `12`; crypto_alt avg `1.184` n `228`; crypto_major avg `1.759` n `8`; equity avg `1.1396` n `74`; fx avg `0.0782` n `6`; index avg `0.3652` n `23`; metal avg `1.5113` n `18`; unknown avg `0.9951` n `593`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
