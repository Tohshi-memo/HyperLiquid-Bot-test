# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T22:56:24.828632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.6621` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `3.51` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.5694` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0489` n `12`; crypto_alt avg `-0.0922` n `228`; crypto_major avg `-0.0819` n `8`; equity avg `0.0557` n `74`; fx avg `0.0145` n `6`; index avg `0.0048` n `23`; metal avg `0.2298` n `18`; unknown avg `13.0826` n `645`
- 1h: commodity avg `0.7451` n `12`; crypto_alt avg `-0.3366` n `228`; crypto_major avg `-0.2935` n `8`; equity avg `0.0207` n `74`; fx avg `0.0656` n `6`; index avg `-0.1653` n `23`; metal avg `0.8678` n `18`; unknown avg `-0.3974` n `645`
- 4h: commodity avg `-0.7657` n `12`; crypto_alt avg `2.9599` n `228`; crypto_major avg `2.8964` n `8`; equity avg `1.327` n `74`; fx avg `0.1373` n `6`; index avg `0.2629` n `23`; metal avg `1.6867` n `18`; unknown avg `3.1612` n `645`
- 24h: commodity avg `-0.7537` n `12`; crypto_alt avg `1.2363` n `228`; crypto_major avg `1.7737` n `8`; equity avg `1.4441` n `74`; fx avg `0.0946` n `6`; index avg `0.365` n `23`; metal avg `1.5624` n `18`; unknown avg `1.2488` n `593`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
