# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T17:53:05.669367+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0088` n `12`; crypto_alt avg `-0.3383` n `228`; crypto_major avg `-0.1291` n `8`; equity avg `-0.0366` n `74`; fx avg `-0.0231` n `6`; index avg `0.0249` n `23`; metal avg `-0.1528` n `18`; unknown avg `-0.2767` n `645`
- 1h: commodity avg `0.03` n `12`; crypto_alt avg `-0.2436` n `228`; crypto_major avg `-0.0748` n `8`; equity avg `-0.0317` n `74`; fx avg `-0.0226` n `6`; index avg `0.013` n `23`; metal avg `-0.139` n `18`; unknown avg `-0.2141` n `645`
- 4h: commodity avg `-0.09` n `12`; crypto_alt avg `-0.545` n `228`; crypto_major avg `-0.5366` n `8`; equity avg `-0.137` n `74`; fx avg `-0.0426` n `6`; index avg `0.0636` n `23`; metal avg `-0.1603` n `18`; unknown avg `-0.0942` n `645`
- 24h: commodity avg `-0.0707` n `12`; crypto_alt avg `-1.6422` n `228`; crypto_major avg `-0.4729` n `8`; equity avg `0.4618` n `74`; fx avg `-0.0405` n `6`; index avg `0.3175` n `23`; metal avg `-0.2932` n `18`; unknown avg `1.2302` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
