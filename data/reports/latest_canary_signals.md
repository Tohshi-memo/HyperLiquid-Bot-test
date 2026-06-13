# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T18:07:37.040131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0596` n `12`; crypto_alt avg `-0.0748` n `228`; crypto_major avg `0.0485` n `8`; equity avg `0.0826` n `74`; fx avg `-0.0052` n `6`; index avg `0.0327` n `23`; metal avg `-0.0107` n `18`; unknown avg `0.0574` n `644`
- 1h: commodity avg `-0.1389` n `12`; crypto_alt avg `0.1433` n `228`; crypto_major avg `0.012` n `8`; equity avg `0.0745` n `74`; fx avg `0.0117` n `6`; index avg `-0.1366` n `23`; metal avg `0.2292` n `18`; unknown avg `0.2227` n `644`
- 4h: commodity avg `-0.2836` n `12`; crypto_alt avg `0.1757` n `228`; crypto_major avg `-0.1649` n `8`; equity avg `0.1041` n `74`; fx avg `-0.0028` n `6`; index avg `-0.0612` n `23`; metal avg `0.1514` n `18`; unknown avg `-1.9743` n `644`
- 24h: commodity avg `-0.9228` n `12`; crypto_alt avg `2.189` n `228`; crypto_major avg `0.145` n `8`; equity avg `0.1029` n `74`; fx avg `0.014` n `6`; index avg `0.5062` n `23`; metal avg `0.4447` n `18`; unknown avg `-1.857` n `611`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
