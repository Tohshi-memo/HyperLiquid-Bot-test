# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T22:22:28.810102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.9346` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `2.66` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.7968` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1675` n `12`; crypto_alt avg `0.3103` n `228`; crypto_major avg `0.5611` n `8`; equity avg `0.0869` n `74`; fx avg `-0.0086` n `6`; index avg `0.0274` n `23`; metal avg `-0.2526` n `18`; unknown avg `0.8761` n `645`
- 1h: commodity avg `0.1058` n `12`; crypto_alt avg `1.1585` n `228`; crypto_major avg `1.3518` n `8`; equity avg `0.9016` n `74`; fx avg `0.1322` n `6`; index avg `0.2995` n `23`; metal avg `1.5277` n `18`; unknown avg `1.1807` n `645`
- 4h: commodity avg `-0.7613` n `12`; crypto_alt avg `3.1859` n `228`; crypto_major avg `3.1733` n `8`; equity avg `1.3765` n `74`; fx avg `0.1161` n `6`; index avg `0.3572` n `23`; metal avg `1.802` n `18`; unknown avg `2.8077` n `645`
- 24h: commodity avg `-1.0485` n `12`; crypto_alt avg `0.9908` n `228`; crypto_major avg `1.7371` n `8`; equity avg `1.4465` n `74`; fx avg `0.0891` n `6`; index avg `0.4587` n `23`; metal avg `1.6816` n `18`; unknown avg `1.7525` n `593`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
