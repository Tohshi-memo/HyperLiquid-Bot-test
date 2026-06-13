# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T19:37:28.676874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0231` n `12`; crypto_alt avg `0.1713` n `228`; crypto_major avg `0.0471` n `8`; equity avg `0.0438` n `74`; fx avg `0.0006` n `6`; index avg `-0.022` n `23`; metal avg `0.016` n `18`; unknown avg `0.048` n `644`
- 1h: commodity avg `-0.0206` n `12`; crypto_alt avg `-0.0276` n `228`; crypto_major avg `-0.0578` n `8`; equity avg `0.0456` n `74`; fx avg `-0.0094` n `6`; index avg `0.0072` n `23`; metal avg `0.0222` n `18`; unknown avg `-0.3463` n `644`
- 4h: commodity avg `-0.2447` n `12`; crypto_alt avg `-0.386` n `228`; crypto_major avg `-0.4608` n `8`; equity avg `0.0128` n `74`; fx avg `0.03` n `6`; index avg `-0.1019` n `23`; metal avg `0.0884` n `18`; unknown avg `-0.4269` n `644`
- 24h: commodity avg `-0.836` n `12`; crypto_alt avg `1.6988` n `228`; crypto_major avg `0.2126` n `8`; equity avg `0.4281` n `74`; fx avg `0.046` n `6`; index avg `0.5762` n `23`; metal avg `0.4649` n `18`; unknown avg `-1.8147` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
