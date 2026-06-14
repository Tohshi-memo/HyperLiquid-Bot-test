# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T06:37:29.001052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0263` n `12`; crypto_alt avg `-0.3144` n `228`; crypto_major avg `-0.2317` n `8`; equity avg `-0.0188` n `74`; fx avg `0.0012` n `6`; index avg `0.0344` n `23`; metal avg `-0.0107` n `18`; unknown avg `3.1836` n `643`
- 1h: commodity avg `-0.0068` n `12`; crypto_alt avg `0.2273` n `228`; crypto_major avg `-0.0132` n `8`; equity avg `0.0336` n `74`; fx avg `0.0015` n `6`; index avg `0.0077` n `23`; metal avg `0.1925` n `18`; unknown avg `1.5019` n `627`
- 4h: commodity avg `-0.0743` n `12`; crypto_alt avg `-0.5347` n `228`; crypto_major avg `-0.6491` n `8`; equity avg `0.0005` n `74`; fx avg `-0.0002` n `6`; index avg `-0.003` n `23`; metal avg `0.0012` n `18`; unknown avg `0.331` n `611`
- 24h: commodity avg `-0.7156` n `12`; crypto_alt avg `1.0233` n `228`; crypto_major avg `1.1835` n `8`; equity avg `0.7551` n `74`; fx avg `-0.0156` n `6`; index avg `0.2402` n `23`; metal avg `0.3225` n `18`; unknown avg `-0.4829` n `601`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
