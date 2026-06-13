# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T21:22:27.711529+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.113` n `12`; crypto_alt avg `-0.1248` n `228`; crypto_major avg `0.0601` n `8`; equity avg `0.0086` n `74`; fx avg `-0.0098` n `6`; index avg `0.0195` n `23`; metal avg `0.1926` n `18`; unknown avg `-0.3264` n `644`
- 1h: commodity avg `0.1584` n `12`; crypto_alt avg `-0.1061` n `228`; crypto_major avg `0.0725` n `8`; equity avg `0.014` n `74`; fx avg `0.0152` n `6`; index avg `0.0297` n `23`; metal avg `-0.0531` n `18`; unknown avg `6.7699` n `644`
- 4h: commodity avg `0.0614` n `12`; crypto_alt avg `-0.3831` n `228`; crypto_major avg `0.2273` n `8`; equity avg `0.2734` n `74`; fx avg `0.0266` n `6`; index avg `0.0518` n `23`; metal avg `-0.075` n `18`; unknown avg `1.1278` n `644`
- 24h: commodity avg `-0.5367` n `12`; crypto_alt avg `1.6958` n `228`; crypto_major avg `0.5688` n `8`; equity avg `0.4954` n `74`; fx avg `0.0858` n `6`; index avg `0.6048` n `23`; metal avg `0.2487` n `18`; unknown avg `-0.2697` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
